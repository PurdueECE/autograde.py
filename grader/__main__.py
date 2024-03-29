import argparse
import csv
from datetime import datetime
import json
import logging
import os
import re
import shutil
import subprocess
import sys
import tempfile


def main(args):
    # arg parsing
    parser = argparse.ArgumentParser(__package__)
    parser.add_argument(
        "path",
        default=".",
        help="Module to grade",
    )
    parser.add_argument(
        "--fallback",
        help="Fallback module to grade",
    )
    parser.add_argument(
        "--submission",
        help="Submission name to grade.",
    )
    parser.add_argument(
        "--tests",
        default=".",
        help="Path of tests to run. Defaults to ./",
    )
    parser.add_argument(
        "--test-pattern",
        default="test*.py",
        help='Test name pattern to match. Defaults to "test*.py"',
    )
    parser.add_argument(
        "--output",
        help="Output file for report. Defaults to stdout.",
    )
    parser.add_argument(
        "--log",
        help="Log file to use. Defaults to stdout.",
    )
    parser.add_argument(
        "--config",
        help="Config file to use.",
    )
    args = parser.parse_args(args)

    # logging
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s:%(levelname)s:%(name)s:%(message)s",
        handlers=[
            logging.StreamHandler(open(args.log, "w+") if args.log else sys.stdout)
        ],
    )
    logging.debug(f"Args:\n{args}\n\n")

    # setup
    try:
        with open(args.config) as f:
            conf = json.load(f)
    except Exception as e:
        logging.exception(f"Error while loding config file: {e}")
        conf = {}
    logging.debug(f"Config:\n{json.dumps(conf, indent=4)}\n\n")
    sconf: dict = conf.get("submissions", {}).get(args.submission, {})
    logging.debug(f"Submission Config:\n{json.dumps(sconf, indent=4)}\n\n")
    scores = {
        "name": sconf.get("name", args.submission or ""),
        "time": datetime.now().isoformat(),
    }

    # run grading
    results = grade(args.fallback, args, conf) if args.fallback else None
    results1 = grade(args.path, args, conf) or {}

    # merge results
    if results:
        for label, test in results.items():
            results[label] = results1.get(label, results[label])
    else:
        results = results1.copy()

    # check results
    if not results:
        logging.error("No tests were run")
        sys.exit(os.EX_OSERR)

    # parse results
    for label, test in results.items():
        scores[label] = test.get("score", 0)

    # store results
    logging.info(f"Scores:\n{json.dumps(scores, indent=4)}\n\n")
    if args.output:
        with open(args.output, "w") as f:
            writer = csv.DictWriter(f=f, fieldnames=scores.keys())
            writer.writeheader()
            writer.writerow(scores)


def grade(path, args, conf):
    results = None

    try:
        cwd = os.getcwd()
        tmp = tempfile.mkdtemp()
        os.chdir(tmp)
        shutil.copytree(f"{cwd}/{path}", "./", dirs_exist_ok=True)
        shutil.copytree(f"{cwd}/{args.tests}", "./", dirs_exist_ok=True)
        proc = subprocess.run(
            f"python3 -m unittest discover -vp {args.test_pattern}",
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            shell=True,
            encoding="utf-8",
        )
        logging.info(proc.stdout)
        results: dict = getResults(proc.stdout, conf)
    except Exception as e:
        logging.exception(f"Exception while grading {path}\n")
        logging.exception(f'{e.output if hasattr(e, "output") else ""}\n')
    finally:
        os.chdir(cwd)
        shutil.rmtree(tmp)

    return results


def getResults(output, conf):
    results = {}
    for testName, result in re.findall(
        r"(.*) \.\.\. [\s|\S]*?(ok|FAIL|ERROR)", output, flags=re.MULTILINE
    ):
        tconf: dict = conf.get("tests", {}).get(testName, {})
        tlabel = tconf.get("name", testName)
        weight = tconf.get("weight", 1)
        results[tlabel] = {
            "score": 1 * weight if result == "ok" else 0,
            "result": result,
        }
    return results


if __name__ == "__main__":
    main(sys.argv[1:])

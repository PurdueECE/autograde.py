from grader.__main__ import main


def test_template():
    main(
        [
            "tests/fixtures/simpleTasks/template",
            "--tests",
            "tests/fixtures/simpleTasks/",
        ]
    )


def test_template_config():
    main(
        [
            "tests/fixtures/simpleTasks/template",
            "--tests",
            "tests/fixtures/simpleTasks/tests_grader.py",
            "--submission",
            "submission1",
            "--config",
            "tests/fixtures/simpleTasks/config.json",
        ]
    )


def test_solution():
    main(
        [
            "tests/fixtures/simpleTasks/solution",
            "--tests",
            "tests/fixtures/simpleTasks/",
            "--log",
            "grader.log",
        ]
    )

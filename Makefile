include .env

test_package:
	python3 -m pip install --upgrade build
	python3 -m build
	python3 -m pip install --upgrade twine
	python3 -m twine upload -u ${USERNAME} -p ${PASSWORD} --repository testpypi dist/*

package:
	python3 -m pip install --upgrade build
	python3 -m build
	python3 -m pip install --upgrade twine
	python3 -m twine upload -u ${USERNAME} -p ${PASSWORD} dist/*

clean:
	rm -rf *.egg-info dist/*
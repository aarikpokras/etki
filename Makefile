all: prepare

prepare:
	rm -rf tests
	mv src/* .
	rmdir src
	rm pyproject.toml
	rm .flake8

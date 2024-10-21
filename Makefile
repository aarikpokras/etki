all: prepare

prepare:
	rm -rf tests
	mv src/* .
	rmdir src

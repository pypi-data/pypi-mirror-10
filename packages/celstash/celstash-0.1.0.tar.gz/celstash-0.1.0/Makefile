all:
	$(error please pick a target)

dist:
	python2 setup.py sdist

test:
	./run-tests.sh	

clean:
	rm -fr build celstash.egg-info dist

upload:
	python setup.py sdist upload



.PHONY: all dist test clean upload

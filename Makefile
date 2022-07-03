.PHONY : test
test : test_1 test.py
test_1 : test_utils.py
	python3 main.py test_utils.py test_1

.PHONY : test
clean:
	rm -rf __pycache__

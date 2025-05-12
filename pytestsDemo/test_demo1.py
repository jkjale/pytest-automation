# Install pytest - pip install pytest

# Any pytest file should start with test_ or end with _test
# pytest method names should start with test
# Any code should be wrapped in method only
# -v stands for more info like metadata
# -s logs in out put
# -k stands for method names execution
# to skip a test you give it the tag @pytest.mark.skip
# to explicitly mark a test as a failure you tag it with @pytest.mark.xfail
# fixtures are used as setup and tear down methods for test cases - conftest.py file to generalize fixture and make it available to all test cases
# datadriven and parameterization can be done with return statements in list format
# when you define fixture scope to class only, it will run once before class is initiated and at the end

'''
To run all tests in a directory, go that directory and in the terminal call:
    - pytest
    - pytest -v
    - pytest -v -s
    - pytest test_demo1.py -v -s
    - pytest -k CreditCard -v -s    --> run all tests that have "CreditCard" in their method name
    - pytest -m smoke -v -s   --> run all tests that have "smoke" tags
    - pytest --html=report.html
'''
import pytest


@pytest.mark.smoke
def test_firstProgram(setup):
    print('Helloo')


@pytest.mark.xfail
def test_SecondGreetCreditCard():
    print('Good morning')


def test_crossBrowser(crossBrowser):
    print(crossBrowser)

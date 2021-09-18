# any pytest file should start with test_ or end with _test
# pytest method names should start with test_
# any code should be wrapped in method only

# py.test test_demo2.py -v -s
# py.test -k CreditCard -v -s

# -k stands for method names execution, -s logs in output, -v stands for more info metadata (verbose)
# you can run specific file tih py.test <filename>

# you can mark(tag) test and then run with -m
# you can skip test with @pytest.mark.skip
# operate but not reporting further @pytest.mark.xfail

# fixtures are used as setup and tear down methods for test cases conftest file to generalize fixture
# and make it available to all test cases

# datadriven and parameterization can be done with return statement in list format
# when you define fixture scope to class only, it will run once before class is initiated and at the end


import pytest


@pytest.mark.smoke
def test_first_program(setup):
    print("Hello")


@pytest.mark.xfail
def test_greetCreditCard():
    print("Good Afternoon")


def test_crossbrowser(cross_browser):
    print(cross_browser[1])


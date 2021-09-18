import pytest


@pytest.mark.smoke
def test_second_program():
    msg = "Hello"           # operations
    assert msg == "Hi", "test failed because string do not match"


def test_second_second_programCreditCard():
    a = 4
    b = 6
    assert a + 2 == 6, "addition do not match"


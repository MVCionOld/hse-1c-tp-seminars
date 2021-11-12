import pytest

from math_functions import add, divide


def test_add():
    assert add(2, 3) == 5


def test_divide():
    assert divide(1, 2) == 0.5
    assert divide(36, 6) == 6

    with pytest.raises(ZeroDivisionError):
        divide(1, 0)


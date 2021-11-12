import pytest

from string_to_int import string_to_int


def test_empty_string():
    with pytest.raises(ValueError) as err:
        string_to_int("")


def test_incorrect_characters():
    test_cases = [
        "a",
        "aaa",
        "42 a",
    ]

    for s in test_cases:
        with pytest.raises(ValueError) as err:
            string_to_int(s)


def test_simple():
    test_cases = [
        ('123', 123),
        ('11', 11),
        ('42', 42),
        ('000000042', 42),
        ('420', 420),
    ]

    for s, result in test_cases:
        assert result == string_to_int(s)

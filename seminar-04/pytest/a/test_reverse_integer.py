from reverse_integer import reverse_integer


def test_reverse():
    assert 321 == reverse_integer(123)
    assert 21 == reverse_integer(120)
    assert 0 == reverse_integer(0)


test_reverse()

from random import randint, seed

from binsearch import binary_search


def linear_search(element, array):
    for index, value in enumerate(array):
        if value == element:
            return index
    return -1


def random_array(length, low, high):
    result = []
    for i in range(length):
        result.append(randint(low, high))
    return result


def test_stress():
    seed(42)

    for i in range(50_000):
        array = sorted(random_array(1_000, -100, 100))
        element = randint(-100, 100)

        assert linear_search(element, array) == binary_search(element, array)


def test_too_stress():
    seed(42)

    for i in range(1_000):
        array = sorted(random_array(50_000, -100, 100))
        element = randint(-100, 100)

        assert linear_search(element, array) == binary_search(element, array)

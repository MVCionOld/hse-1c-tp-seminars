def factorial(number):
    # fix this
    production = 0
    for i in range(number):
        production *= i
    return production


if __name__ == "__main__":
    assert 2 == factorial(2)
    assert 3628800 == factorial(10)
    assert 1 == factorial(0)
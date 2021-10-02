from math import log, isclose, e


def log_of_production(array):
    # fix this
    production = 1
    for element in array:
        production *= element
    return log(production)


if __name__ == "__main__":
    assert isclose(1, log_of_production([e]))
    assert isclose(5, log_of_production([e, e, e, e, e]))
    assert isclose(-840.4435589428239, log_of_production([0.1] * 365))
    assert isclose(
        -770.7294293239338,
        log_of_production([1e-10, 1e-11, 5e-12, 3e-18, 9e-64, 7e-128, 2e-95]),
    )
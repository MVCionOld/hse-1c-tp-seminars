def reverse_integer(x):
    result = 0

    while x > 0:
        result *= 10
        result += x % 10
        x //= 10

    return result

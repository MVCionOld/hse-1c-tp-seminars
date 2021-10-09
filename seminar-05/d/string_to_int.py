def string_to_int(s):
    result = 0

    if s == "":
        raise ValueError("string is empty")

    for i in s:
        if i not in "0123456789":
            raise ValueError("string contains not a number")

        result *= 10
        result += int(i)

    return result

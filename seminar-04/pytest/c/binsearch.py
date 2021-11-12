def binary_search(element, array):
    left, right = 0, len(array)

    while left + 1 < right:
        middle = (left + right) // 2

        if array[middle] < element:
            left = middle
        else:
            right = middle

    if array[left] == element:
        return left

    if right < len(array) and array[right] == element:
        return right

    return -1

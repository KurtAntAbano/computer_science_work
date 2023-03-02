def binary_search(list, target):
    low = 0
    high = len(list) - 1
    # variables declared

    while low <= high:
        # repeats while low is not greater then high
        mid = (high + low) // 2
        if list[mid] < target:
            low = mid + 1
        elif list[mid] > target:
            high = mid - 1
            # adjusting pointers depending on the comparison
        else:
            return mid
    return -1


print(binary_search([2, 3, 4, 12, 23, 43, 332, 1, 6], 23))

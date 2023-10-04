def binary_search(list, low, high, target):
    if high >= low:
        mid = (high + low) // 2
        if list[mid] == target:
            return mid
        # checks if the item is found
        elif list[mid] > target:
            return binary_search(list, low, mid - 1, target)
        else:
            return binary_search(list, mid + 1, high, target)
        # returning the same function but with different high or low parameters

    else:
        return -1


list = [1, 4, 6, 7, 9, 12]
print(binary_search(list, 0 , len(list) - 1, 9))

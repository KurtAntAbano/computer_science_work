def bubble_sort(list):
    num_items = len(list) - 1
    swap = True

    while swap:
        swap = False
        for index in range(0, num_items):
            if list[index] > list[index + 1]:
                temp = list[index]
                list[index] = list[index + 1]
                list[index + 1] = temp  # Swap the items
                swap = True
    return list


print(bubble_sort([4, 5, 3, 12, 6, 20]))

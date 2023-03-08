def insertion_sort(list):
    num_items = len(list)
    for index in range(1, num_items):  # starts at 1 because we start at the second item

        item_to_insert = list[index]
        position = index - 1  # the last sorted item

        while position >= 0 and list[position] > item_to_insert:
            list[position + 1] = list[position]
            position = position - 1


        list[position + 1] = item_to_insert
    return list


list = [4, 7, 8, 2, 1, 5, 9]
print(insertion_sort(list))
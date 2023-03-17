def linear_search(data_set, item_sought, i):
    if data_set[i] == item_sought:
        return i
    elif i == len(data_set)-1:
        return -1
    else:
        return linear_search(data_set, item_sought, i + 1)


print(linear_search([12, 23, 55, 65, 3, 4, 59, 100], 55, 0))

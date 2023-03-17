def linear_search(data_set, item_sought):
    index = -1
    i = 0
    found = False
    while i < len(data_set) and found == False:
        if data_set[i] == item_sought:
            index = i
            found = True
        i += 1
    return index


print(linear_search([200, 12, 34, 543, 342, 55, 800], 800))
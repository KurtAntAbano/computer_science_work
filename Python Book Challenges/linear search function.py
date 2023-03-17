def linear_search(data_set, item_sought):
    i = 0
    found = False
    while i < len(data_set) and found == False:
        if data_set[i] == item_sought:
            found = True
        i = i + 1
    return found


print(linear_search([200, 12, 34, 543, 342, 55, 800], 800))

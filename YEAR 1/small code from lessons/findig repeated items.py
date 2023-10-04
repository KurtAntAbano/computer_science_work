def repeat_search(data_set):
    for i in range(0, len(data_set)):
        count = 0
        item = data_set[i]
        for j in range(0, len(data_set)):
            if data_set[j] == item:
                count += 1
        print(item, count)


if __name__ == "__main__":
    repeat_search([17, 44, 5, 44, 6, 12, 12, 12])

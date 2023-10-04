def largest_search(data_set):
    largest = data_set[0]

    for i in range(0, len(data_set)):
        if data_set[i] > largest:
            largest = data_set[i]
    print(largest)


if __name__ == "__main__":
    largest_search([1,4,6,99,43,54,1,120])

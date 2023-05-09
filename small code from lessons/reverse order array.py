def output_reverse(array):
    for i in range(5, -1, -1):
        print(array[i])


def total_and_average(array):
    total = 0
    for i in range(0, 5):
        total += array[i]

    average = total / 6
    print(f"average is {average}\ntotal is {total}")


output_reverse([1, 2, 3, 4, 5, 6])
total_and_average([1, 2, 3, 4, 5, 6])



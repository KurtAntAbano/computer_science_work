def bubble_sort(list):
    largest = list[0]
    length = len(list) - 1
    largest_pointer = list[length]
    while largest_pointer > 0:
        for i in range(0, largest_pointer):
            if largest < list[i+1]:
                temp = largest
                largest = list[i+1]
                list[i+1] = temp

        temp = largest_pointer
        largest_pointer = largest
        largest = temp
        largest_pointer = list[length - 1]

print(bubble_sort([4,6,9,2,8,3]))

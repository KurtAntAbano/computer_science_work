import random
import timeit

def insertion_sort(list):
    num_items = len(list)
    for index in range(1, num_items):  # starts at 1 because we start at the second item

        item_to_insert = list[index]
        position = index - 1  # the last sorted item

        while position >= 0 and list[position] > item_to_insert:
            list[position + 1] = list[position]
            position -= 1


        list[position + 1] = item_to_insert
        # list[position +1] was where
    return list

def timeMeasure():
    start = timeit.default_timer()
    end = timeit.default_timer()
    t = (end -start)*1000000 # time in microseconds. To convert it milliseconds multiply times 1000, and for second multiply by 1
    print("Time of execution is " + str(t)+ " microseconds")


list = []
for i in range(0,10):
    x = random.randint(0,100)
    list.append(x)
# this creates a random array

if __name__ == "__main__":
    print("unsorted:", list)
    print("sorted:", insertion_sort(list))
    timeMeasure()


#MAKE A SWAP AND COMPRISON variable

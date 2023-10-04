import random
#from to_import timemeasure

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



list = []
for i in range(0,10):
    x = random.randint(0,100)
    list.append(x)
# this creates a random array

if __name__ == "__main__":
    print("unsorted:", list)
    print("sorted:", insertion_sort(list))
    #timemeasure()


#MAKE A SWAP AND COMPRISON variable



def merge(list1, list2):  # this function only merges two lists
    p1 = 0
    p2 = 0
    list3 = []

    while p1 < len(list1) and p2 < len(list2):
        if list1[p1] < list2[p2]:
            list3.append(list1[p1])
            p1 += 1
        else:
            list3.append(list2[p2])
            p2 += 1

    if len(list1) > len(list2):  # this adds any left-over elements
        list3.append(list1[p1:])

    else:
        list3.append(list2[p2:])

    return list3


if __name__ == "__main__":
    list1 = [2, 3, 4, 8]
    list2 = [1, 5, 6, 7, 9, 10, 12, 20]
    print(merge(list1, list2))

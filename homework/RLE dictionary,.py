def rle_encode(data):
    prev_num = data[0]
    count = 1
    dictionary = {}

    for i in range(1, len(data)):
        item = data[i]
        if item == prev_num:
            count += 1

        else:
            dictionary[prev_num] = count
            count = 1
            prev_num = item

    dictionary[item] = count
    return dictionary


print(rle_encode("aabbbccc"))

# list = [2, 3, 5]
# item = list[0]
# dictionary = {}
# dictionary[item] = None
# print(dictionary)

def repeat_search(data_set):
    dictionary = {}
    for i in range(0, len(data_set)):
        item = data_set[i]
        if item not in dictionary.keys():
            for j in range(0, len(data_set)):
                count = 0
                if data_set[j] == item:
                    count += 1
            dictionary[item] = count


    print(dictionary)



    # for j in range(0, len(data_set)):
    #     count = 0
    #     item = data_set[j]
    #     for g in range(0, len(data_set)):
    #         if data_set[g] == item:
    #             count += 1





repeat_search([2, 2, 3, 4, 4 , 3, 2, 7])
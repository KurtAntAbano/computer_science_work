input_num = int(input("Please input number"))


def string_conversion_sqaure(num):
    num = str(num)
    num_list = []
    length = len(num)

    for i in range(0, length):
        num_list.append(int(num[i]))

    total = 0
    length = len(num_list)

    for i in range(0, length):
        num_sqaure = num_list[i] ** 2
        total = total + num_sqaure

    print(total)
    return total


total = string_conversion_sqaure(input_num)

while (total != 1 and total != 4):
    total = string_conversion_sqaure(total)

if (total == 1 and total != 4):
    print(str(input_num) + " is a happy number")

elif (total == 4 and total != 1):
    print(str(input_num) + " is not a happy number")

















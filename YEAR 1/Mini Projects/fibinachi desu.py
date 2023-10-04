count_input = int(input("How many terms would you like"))
x = 0
y = 1

list = []
for i in range(0, count_input):
    next_num = x + y
    x = y
    y = next_num

    list.append(y)
print(list)


count_input = int(input("How many terms would you like"))
x, y, count = 0, 1, 0
fib_list = [0]
while count_input != count:
    next_num = x + y
    x = y
    y = next_num
    count += 1
    fib_list.append(next_num)

print("Fibonacci sequence =",fib_list)

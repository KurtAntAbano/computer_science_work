string = input("input a string")
stack = []
length = len(string)
stack_pointers = -1
for i in range(0, length):
    stack.append(string[i])
    stack_pointers += 1


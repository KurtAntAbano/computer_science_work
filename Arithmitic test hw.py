import random
score = 0
count = 0

x = random.randint(1,10)
y = random.randint(1,10)

def add(x,y):
    return x + y
def sub(x, y):
    return x - y
def mul(x, y):
    return x * y
def div(x, y):
    return x // y

operation_list = ["add","sub","mul","div"]

while count != 10:
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    option = random.choice(operation_list)

    if option == "add":
        print(x,"+", y, "=")
        right_answer = add(x,y)
        answer = int(input())
        if answer == right_answer:
            score += 1
            count += 1
        else:
            count += 1

    if option == "sub":
        print(x,"-",y,"=")
        right_answer = sub(x,y)
        answer = int(input())
        if answer == right_answer:
            score += 1
            count += 1
        else:
            count += 1

    if option == "mul":
        print(x,"*",y,"=")
        right_answer = mul(x,y)
        answer = int(input())
        if answer == right_answer:
            score += 1
            count += 1
        else:
            count += 1

    if option == "div":
        print(x,"/", y,"=")
        right_answer = div(x,y)
        answer = int(input())
        if answer == right_answer:
            score += 1
            count += 1
        else:
            count += 1

print("you got", score,"out of 10!")
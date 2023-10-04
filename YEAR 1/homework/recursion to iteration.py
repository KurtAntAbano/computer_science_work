def calcultae(num1, num2):
    while num1 != num2:
        if num1 < num2:
            num2 = num2-num1
        elif num1 > num2:
            num1 = num1 - num2

    return num1

print(calcultae(2,13))
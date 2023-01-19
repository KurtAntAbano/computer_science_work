result = 0
def thisFunction(theArray, num1, num2, num3):
    while theArray[result] != num3:
        result = num1 + ((num2 - num1) // 2))
        if num2 > num1:
            if theArray[result] < num3:
                num1 = result + 1
            else:
                num2 = result - 1
        else:
            result = -1
            return result
    return result



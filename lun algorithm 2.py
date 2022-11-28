

def calculations(digits):
    total = 0
    for i in range(0, 11):
        total += int(digits[i])
    print(total)
    return total


def length_check(digits):
    length = len(digits)
    if length != 11:
        print("INVALID LENGTH")
        temp = False
    else:
        print("VALID LENGTH")
        temp = True
    return temp


def is_valid(total):
    result = total % 10
    if result == 0:
        return True
    else:
        return False


def main():
    digits = input("Please input 11 digits")
    total = calculations(digits)

main()

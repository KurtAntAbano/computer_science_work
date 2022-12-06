# def calculations(digits):

#   total = 0

#  for i in range(0, 11):

#     total += int(digits[i])

# print(total)

# return is_valid(total)


def calculations(digits):
    total = 0

    total += int(digits[0])

    for i in range(1, 11):

        if i % 2 == 1:

            temp = int(digits[i]) * 2

            total += int(digits[i])

            if temp > 9:

                temp_str = str(temp)

                total += int(temp_str[0]) + int(temp_str[1])

            else:

                total += int(digits[i])



        elif i % 2 == 0:

            total += int(digits[i])

    print(total)

    return is_valid(total)


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


count = 0


def main(count):
    digits = input("Please input 11 digits")

    if not length_check(digits):

        count += 1

        if count == 3:
            print("sorry, too many attempts")

            exit()

        main(count)

    total = calculations(digits)

    if total == True:

        print("This is valid")

    else:

        print("This is Invalid")

        count += 1

        if count == 3:
            print("sorry, too many attempts")

            exit()

        main(count)


main(count)
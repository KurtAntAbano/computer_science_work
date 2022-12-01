# declaring empty list, and intialising stackPointer.
names = ["", "", "", "", "", "", "", "", "", "", ""]
stackPointer = 0
maxLength = len(names)

# the above are global

def push(element):
    global stackPointer
    global maxLength
    global names

    names[stackPointer] = element
    stackPointer += 1

    print("New stack:\n", names)


# write code to check push an element (passed as parameter) at the stackPoonter


def pop():
    global stackPointer
    global maxLength
    global names


# write a code to pop the element at stackPointer


def isEmpty():
    global stackPointer
    global maxLength
    global names

    if stackPointer == 0:
        print("Stack is empty")

    else:
        x = maxLength - stackPointer
        print("there are", x, "spaces left")





    # write code to check if stack is empty, if so return True
    # otherwise return False


def isFull():
    global stackPointer
    global maxLength
    global names

    if stackPointer != maxLength:
        return False
    else:
        return True

    # write code to check if stack is full,
    # if so return True otherwise return False


def main():
    global stackPointer
    global maxLength
    global names

    isEmpty()

    if not isFull():
        element = input("type something to add")
        push(element)
        again = input("Would you like to add another element? y/n")
        if again == "y":
            main()
        else:
            print("Thank you for using my program!")

    elif isFull():
        print("Stack is full")


main()



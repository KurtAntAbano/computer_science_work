# declaring empty list, and intialising stackPointer.
names = ["", "", "", "", "", "", "", "", "", "", ""]
stackPointer = 0
maxLength = len(names)


# the above are global

def push(element):
    global stackPointer
    global maxLength
    global names

    if isFull():
        print("ERROR STACK IS FULL")

    else:
        names[stackPointer] = element
        stackPointer += 1

        print("New stack:\n", names)


# write code to check push an element (passed as parameter) at the stackPoonter


def pop():
    global stackPointer
    global maxLength
    global names

    if isEmpty():
        print("ERROR, Stack is empty")
    else:
        stackPointer -= 1
        print(names[stackPointer], "has been undone")



# write a code to pop the element at stackPointer


def isEmpty():
    global stackPointer
    global maxLength
    global names

    if stackPointer == 0:
        return True

    else:
        return False

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

    print("What would you like to do:\n1.push\n2.pop\n3.check if empty\n4.check if full")
    answer = input()
    if answer == "1":
        element = input("type something to add")
        push(element)

    elif answer == "2":
        pop()
    elif answer == "3":
        if isEmpty():
            print("Stack is empty")
        else:
            print("Stack is not empty")

    elif answer == "4":
        if isFull():
            print("Stack is full")
        else:
            print("Stack is not full")

    again = input("would you like to go again? y/n")
    if again == "y":
        main()
    else:
        print("Thank you for using my program")


main()


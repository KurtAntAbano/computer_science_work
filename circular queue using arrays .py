# declaring empty list, and intialising stackPointer.
names = ["", "", ""]
head = 0
tail = 0
maxLength = len(names)


# the above are global

def push(element):
    global names, tail, maxLength
    if isFull():
        print("ERROR STACK IS FULL")

    else:
        names[tail] = element
        tail += 1
        if tail == maxLength:
            tail = 0

        print("Queue:\n", names)

    # write code to check push an element (passed as parameter) at the stackPoonter


def pop():
    global head, maxLength, names


    if isEmpty():
        print("ERROR, queue is empty")
    else:
        print(names[head], "has been removed")
        head += 1
        if head > maxLength:
            head = 0

    # write a code to pop the element at stackPointer


def isEmpty():
    global head,tail

    if head == tail:
        return True

    else:
        return False

        # write code to check if stack is empty, if so return True
    # otherwise return False


def isFull():
    global head, tail, maxLength

    if head == 0 and tail == maxLength or head == tail + 1:
        return True
    else:
        return False

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
            print("queue is empty")
        else:
            print("queue is not empty")

    elif answer == "4":
        if isFull():
            print("queue is full")
        else:
            print("queue is not full")

    again = input("would you like to go again? y/n")
    if again == "y":
        main()
    else:
        print("Thank you for using my program")


main()
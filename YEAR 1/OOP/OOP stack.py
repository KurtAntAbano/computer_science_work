class Stack():

    def __init__(self, size):  # size is a local variable set by the user
        self.__sp = 0  # initial value of stack pointer
        self.__alist = []  # empty list
        self.stacksize = size
        while len(self.__alist) < size:
            self.__alist.append(" ")

# to access in the class use self.attribute
# to access outside the class use objectname.attribute

    def isEmpty(self):
        if self.__sp == 0:
            return True
        else:
            return False


    def isFull(self):
        if self.__sp == self.stacksize:
            return True
        else:
            return False


    def push(self, item):
        if self.isFull():
            print("error")
        else:
            self.__alist[self.__sp] = item
            self.__sp += 1


    def pop(self):
        if self.isEmpty():
            print("error")
        else:
            self.__sp -= 1
            print(self.__alist[self.__sp])

    def get_alist(self):
        return self.__alist

    def get_sp(self):
        return self.__sp


if __name__ == "__main__":
    myStack = Stack(5)
    print(myStack.isEmpty())
    myStack.push("hello")
    myStack.push("world")
    print(myStack.get_alist())
    print(myStack.get_sp())


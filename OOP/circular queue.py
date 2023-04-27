class Queue:
    def __init__(self, size):
        self.head = 0
        self.tail = 0
        self.alist = []
        self.size = size
        while len(self.alist) < size:
            self.alist.append(" ")


    def isEmpty(self):
        if self.head == self.tail:
            return True
        else:
            return False


    def isFull(self):
        if self.head == 0 and self.tail == (self.size - 1) or self.head == self.tail + 1:
            return True
        else:
            return False


    def enqueue(self, item):
        if self.isEmpty():
            print("error")
        else:
            self.alist[self.tail] = item
            if self.tail == (self.size - 1):
                self.tail = 0
            else:
                self.tail += 1


    def dequeue(self):
        if self.isFull():
            print("error")
        else:
            print(self.alist[self.head], "has been removed")
            if self.head == (self.size - 1):
                self.head = 0
            else:
                self.head += 1





if __name__ == "__main__":
    myQueue = Queue(10)
    print(myQueue.alist)
    print(myQueue.isEmpty())
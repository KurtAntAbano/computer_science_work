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
        if self.head == 0 and self.tail == (self.size ) or self.head == self.tail + 1:
            return True
        else:
            return False


    def enqueue(self, item):
        if self.isFull():
            print("error, queue is full")
        else:
            if self.tail == (self.size):
                self.tail = 0
            else:
                self.alist[self.tail] = item
                self.tail += 1


    def dequeue(self):
        if self.isEmpty():
            print("error, queue is empty")
        else:
            print(self.alist[self.head], "has been removed")
            if self.head == (self.size):
                self.head = 0
            else:
                self.head += 1





if __name__ == "__main__":
    # myQueue = Queue(2)
    # myQueue.dequeue()
    # print(myQueue.alist)
    # print(myQueue.isEmpty())
    # myQueue.enqueue("hello")
    # myQueue.enqueue("world")
    # print(myQueue.alist)
    # myQueue.enqueue("test")
    #
    # print(myQueue.isFull())

    myQueue2 = Queue(3)
    myQueue2.enqueue("Hello")
    myQueue2.enqueue("world")
    myQueue2.enqueue("!!!")

    myQueue2.dequeue()
    print(myQueue2.head)
    print(myQueue2.isFull())
    myQueue2.enqueue("yes")
    print(myQueue2.alist)


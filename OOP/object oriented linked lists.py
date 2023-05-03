class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next  = next

    def __str__(self):
        return str(self.data)

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        newNode = Node(data)
        if self.head is not None:
            current = self.head
            while (current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    def print(self):
        current = self.head
        while current != None:
            print(current.data)
            current = current.next



if __name__ == "__main__":
    fruit = LinkedList
    fruit.insert("apple")
    fruit.insert("orange")
    fruit.insert("grape")

    fruit.print()
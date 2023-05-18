class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = None  # none as the list is empty for now

    def insert(self, data):
        newNode = Node(data)
        if self.head is not None:  # this checks if the list is not empty
            current = self.head  # this takes the first item in the list / head

            while current.next is not None:  # while the current item has a pointer
                current = current.next  # move onto the next element
            current.next = newNode  # the end of the list is reached, where newNode is finally added to the end
        else:
            self.head = newNode  # establishes the head

    def print(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

    def is_present(self, target):
        current = self.head
        flag = False
        while flag is False:  # flag allows program to iterate
            if current.data == target:  # this checks if we have found the target
                print(target, "is present in this list")
                flag = True

            elif current.next is None:  # if the current element is pointing to None then we have checked the whole list
                print(target,"could not be found")
                flag = True

            else:
                current = current.next  # this moves onto the next element


    def delete(self, element):
        current = self.head
        previous = None
        while current is not None:
            if current.data == element:

                if previous is not None:  # this checks if the element we wanted to remove is not the head
                    previous.next = current.next
                else:  # if it is the head then the next element becomes the new head
                    self.head = current.next
            previous = current
            current = current.next





if __name__ == "__main__":
    fruit = LinkedList()
    fruit.insert("apple")
    fruit.insert("orange")
    fruit.insert("grape")

    fruit.print()
    fruit.is_present("grape")

    fruit.delete("apple")
    fruit.print()







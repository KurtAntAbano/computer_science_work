


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next  = next
    def __str__(self):
        return str(self.data)


def print_List(head): #node gives the head node
    node = head
    while node != None:
        print(node.data)
        node = node.next





if __name__ == "__main__":
    node1 = Node("apple")

    node2 = Node("Orange")
    node3 = Node("Pear")
    node1.next = node2
    node2.next = node3

    print_List(node1)




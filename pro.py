class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularlyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        node = Node(data)
        if self.head is None:
            node.next = node
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.tail.next = node
            self.tail = node

    def printCll(self):
        temp = self.head
        print(temp.data)
        while(temp.next != self.head):
            temp = temp.next
            print(temp.data)

# Example usage
cll = CircularlyLinkedList()
cll.insert(1)
cll.insert(2)
cll.insert3)
cll.printCll()

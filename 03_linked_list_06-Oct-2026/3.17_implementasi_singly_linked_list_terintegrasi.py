class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def insert_after(self, target, data):
        current = self.head
        while current is not None:
            if current.data == target:
                new_node = Node(data)
                new_node.next = current.next
                current.next = new_node
                return True
            current = current.next
        return False

    def search(self, target):
        current = self.head
        position = 0
        while current is not None:
            if current.data == target:
                return position
            current = current.next
            position += 1
        return -1

    def update(self, old_value, new_value):
        current = self.head
        while current is not None:
            if current.data == old_value:
                current.data = new_value
                return True
            current = current.next
        return False

    def delete(self, target):
        if self.head is None:
            return False
        if self.head.data == target:
            self.head = self.head.next
            return True
        previous = self.head
        current = self.head.next
        while current is not None:
            if current.data == target:
                previous.next = current.next
                return True
            previous = current
            current = current.next
        return False

    def length(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=' -> ')
            current = current.next
        print('None')


data = SinglyLinkedList()
data.append(10)
data.append(20)
data.append(30)
data.insert_beginning(5)
data.insert_after(20, 25)
data.display()
print('Posisi 25:', data.search(25))
print('Jumlah node:', data.length())
data.update(25, 27)
data.delete(20)
data.display()

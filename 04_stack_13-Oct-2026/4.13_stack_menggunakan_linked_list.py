class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedStack:
    def __init__(self):
        self.top = None
        self.count = 0

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.count += 1

    def pop(self):
        if self.is_empty():
            return None
        data = self.top.data
        self.top = self.top.next
        self.count -= 1
        return data

    def peek(self):
        if self.is_empty():
            return None
        return self.top.data

    def size(self):
        return self.count

stack = LinkedStack()
stack.push(10)
stack.push(20)
stack.push(30)

print('Data paling atas:', stack.peek())
print('Jumlah data:', stack.size())

print('Hasil pop:', stack.pop())
print('Data paling atas:', stack.peek())
print('Jumlah data:', stack.size())

while not stack.is_empty():
    print('Hasil pop:', stack.pop())
print('Stack kosong:', stack.is_empty())

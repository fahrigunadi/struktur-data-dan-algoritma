class Kotak:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert_beginning(self, data):
        new_kotak = Kotak(data)
        new_kotak.next = self.head
        self.head = new_kotak

    def append(self, data):
        new_kotak = Kotak(data)
        if self.head is None:
            self.head = new_kotak
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_kotak

    def insert_after(self, target, data):
        current = self.head
        while current is not None:
            if current.data == target:
                new_kotak = Kotak(data)
                new_kotak.next = current.next
                current.next = new_kotak
                return True
            current = current.next
        return False

    def search(self, target):
        current = self.head
        posisi = 0
        while current is not None:
            if current.data == target:
                return posisi
            current = current.next
            posisi += 1
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
        sebelum = self.head
        current = self.head.next
        while current is not None:
            if current.data == target:
                sebelum.next = current.next
                return True
            sebelum = current
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

l = SinglyLinkedList()
l.append(100)
l.append(200)
l.append(300)

l.display()

l.insert_beginning(50)
l.insert_after(200, 250)
l.display()
print('Posisi 250:', l.search(250))
print('Jumlah kotak:', l.length())
l.update(250, 270)
l.delete(200)
l.display()

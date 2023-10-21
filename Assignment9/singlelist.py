from node import Node

class SingleList:
    """Klasa reprezentująca całą listę jednokierunkową."""

    def __init__(self):
        self.length = 0   # nie trzeba obliczać za każdym razem
        self.head = None
        self.tail = None

    def is_empty(self):
        #return self.length == 0
        return self.head is None

    def count(self):   # tworzymy interfejs do odczytu
        return self.length

    def insert_head(self, node):
        if self.head:   # dajemy na koniec listy
            node.next = self.head
            self.head = node
        else:   # pusta lista
            self.head = self.tail = node
        self.length += 1

    def insert_tail(self, node):   # klasy O(1)
        if self.head:   # dajemy na koniec listy
            self.tail.next = node
            self.tail = node
        else:   # pusta lista
            self.head = self.tail = node
        self.length += 1

    def remove_head(self):   # klasy O(1)
        if self.is_empty():
            raise ValueError("pusta lista")
        node = self.head
        if self.head == self.tail:   # self.length == 1
            self.head = self.tail = None
        else:
            self.head = self.head.next
        node.next = None   # czyszczenie łącza
        self.length -= 1
        return node   # zwracamy usuwany node

    # ZADANIE
    def remove_tail(self):
        if self.is_empty():
            raise ValueError("List is empty")
        current_node = self.head
        while current_node.next is not None and current_node.next != self.tail:
            current_node = current_node.next
        node = self.tail
        self.tail = current_node
        self.length -= 1

        return node

    def clear(self):
        self.remove_head()

    def join(self, other: "SingleList"):
        if self.is_empty():
            self.head = other.head
            self.tail = other.tail
            self.length = other.length

        elif not other.is_empty():
            self.tail.next = other.head
            self.tail = other.tail
            self.length += other.length

        # Wyczyszczenie na koniec
        other.clear()


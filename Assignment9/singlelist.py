from node import Node


class SingleList:
    """Klasa reprezentująca całą listę jednokierunkową."""

    def __init__(self):
        self.length = 0  # nie trzeba obliczać za każdym razem
        self.head = None
        self.tail = None

    def is_empty(self):
        # return self.length == 0
        return self.head is None

    def insert_head(self, node):
        if self.head:  # dajemy na koniec listy
            node.next = self.head
            self.head = node
        else:  # pusta lista
            self.head = self.tail = node
        self.length += 1

    def insert_tail(self, node):  # klasy O(1)
        if self.head:  # dajemy na koniec listy
            self.tail.next = node
            self.tail = node
        else:  # pusta lista
            self.head = self.tail = node
        self.length += 1

    # ZADANIE 11.1 ----------------------------
    def remove_tail(self):
        if self.is_empty():
            raise ValueError("Empty List")
        removed_node = self.tail

        if self.head == self.tail:
            self.head = self.tail = None
        else:
            current_node = self.head
            while current_node.next != self.tail:
                current_node = current_node.next
            self.tail = current_node
            self.tail.next = None

        self.length -= 1
        return removed_node

    def clear(self):
        self.head = self.tail = None
        self.length = 0

    def join(self, other: "SingleList"):
        if other.is_empty():
            return
        if self.is_empty():
            self.head = other.head
            self.tail = other.tail
        else:
            self.tail.next = other.head
            self.tail = other.tail

        self.length += other.length
        other.clear()

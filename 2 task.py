# Определение класса узла списка
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


# Определение класса однонаправленного списка
class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def remove_first_less_than(self, value):
        if self.is_empty():
            return

        # Если первый элемент удовлетворяет условию
        if ord(self.head.data) < value:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if ord(current.next.data) < value:
                current.next = current.next.next
                return
            current = current.next

    def insert_after_digits(self):
        if self.is_empty():
            return

        current = self.head
        while current:
            if current.data.isdigit():
                new_node = Node('%')
                new_node.next = current.next
                current.next = new_node
                current = current.next  # Переходим к следующему символу после вставки
            current = current.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Создание списка и добавление элементов
linked_list = LinkedList()
characters = ['a', '1', 'b', 'c', '5', 'd', 'e', '2']

for char in characters:
    linked_list.insert_at_end(char)

# Вывод исходного списка
print("Исходный список:")
linked_list.display()

# Удаление первого элемента, код которого меньше 48
linked_list.remove_first_less_than(48)

# Вставка символа % после каждой цифры
linked_list.insert_after_digits()

# Вывод списка после операций удаления и вставки
print("\nСписок после удаления и вставки:")
linked_list.display()

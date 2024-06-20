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

    def insert_before_value(self, value, new_data):
        new_node = Node(new_data)
        if self.is_empty():
            return

        # Если значение, перед которым нужно вставить новый элемент, находится в начале списка
        if self.head.data == value:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        while current.next:
            if current.next.data == value:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Создание списка и добавление элементов
linked_list = LinkedList()
numbers = [10.5, 55, 20.3, 55, 30.7, 40.2, 55, 50.9]

for number in numbers:
    linked_list.insert_at_end(number)

# Вывод исходного списка
print("Исходный список:")
linked_list.display()

# Вставка числа 0.99 перед каждым элементом со значением 55
current = linked_list.head
while current:
    if current.data == 55:
        linked_list.insert_before_value(55, 0.99)
        current = current.next  # Пропускаем вставленный элемент, чтобы не вставлять перед ним снова
    current = current.next

# Вывод списка после вставок
print("\nСписок после вставок:")
linked_list.display()

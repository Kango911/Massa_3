# Определение класса узла двусвязного списка
class Node:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None


# Определение класса двусвязного списка
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
        self.tail = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # Kango911
    def move_elements_between(self, px, py):
        if px is None or py is None:
            return None

        new_list = DoublyLinkedList()

        # Находим элементы между px и py
        current = px.next
        while current != py:
            new_list.insert_at_end(current.data)
            current = current.next

        # Устанавливаем указатель на первый элемент преобразованного списка
        transformed_list_pointer = new_list.head
        # Если новый список пуст, устанавливаем указатель на nil
        if transformed_list_pointer is None:
            transformed_list_pointer = "nil"

        # Выводим указатели на первые элементы преобразованного и нового списков
        print(f"Указатель на первый элемент преобразованного списка: {transformed_list_pointer}")
        print(f"Указатель на первый элемент нового списка: {new_list.head if new_list.head else 'nil'}")

    def find_node_by_data(self, data):
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next
        return None


# Создание и заполнение двусвязного списка
doubly_linked_list = DoublyLinkedList()
elements = [10, 20, 30, 40, 50, 60, 70, 80, 90]
#Kango911
for elem in elements:
    doubly_linked_list.insert_at_end(elem)

# Вывод исходного списка
print("Исходный список:")
doubly_linked_list.display()

# Находим указатели PX и PY
px = doubly_linked_list.find_node_by_data(30)  # Например, элемент со значением 30
py = doubly_linked_list.find_node_by_data(80)  # Например, элемент со значением 80

# Перемещаем элементы между PX и PY в новый список и выводим указатели на первые элементы
doubly_linked_list.move_elements_between(px, py)

# Task 1: Node sinfini yaratmaq
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        current = self.head
        res = []
        while current:
            res.append(str(current.data))
            current = current.next
        res.append("None")
        print(" -> ".join(res))

    # Task 2: Siyahının sonuna element əlavə etmək
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # Task 3: Siyahının əvvəlinə element əlavə etmək
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Task 4: Verilmiş elementdən sonra əlavə etmək
    def insert_after(self, target, data):
        current = self.head
        while current:
            if current.data == target:
                new_node = Node(data)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next

    # Task 5: Element silmək
    def delete_node(self, key):
        current = self.head
        if current and current.data == key:
            self.head = current.next
            return
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        if current:
            prev.next = current.next

    # Task 6: Axtarış
    def search(self, value):
        current = self.head
        while current:
            if current.data == value:
                print("Element tapıldı.")
                return True
            current = current.next
        print("Element tapılmadı.")
        return False

    # Task 7: Uzunluğun hesablanması
    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        print(f"List length = {count}")
        return count

    # Task 8: Maksimum və minimum element
    def find_min_max(self):
        if not self.head:
            return
        min_val = self.head.data
        max_val = self.head.data
        current = self.head.next
        while current:
            if current.data < min_val:
                min_val = current.data
            if current.data > max_val:
                max_val = current.data
            current = current.next
        print(f"Minimum: {min_val}, Maksimum: {max_val}")

    # Task 9: Siyahını tərs çevirmək
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev


# Task 10 (Challenge): Tələbə qeydiyyat sistemi
class StudentNode:
    def __init__(self, student_id, student_name, gpa):
        self.student_id = student_id
        self.student_name = student_name
        self.gpa = gpa
        self.next = None

class StudentRegistry:
    def __init__(self):
        self.head = None

    def add_student(self, student_id, student_name, gpa):
        new_node = StudentNode(student_id, student_name, gpa)
        new_node.next = self.head
        self.head = new_node

    def delete_student(self, student_id):
        current = self.head
        if current and current.student_id == student_id:
            self.head = current.next
            return
        prev = None
        while current and current.student_id != student_id:
            prev = current
            current = current.next
        if current:
            prev.next = current.next

    def display_students(self):
        current = self.head
        while current:
            print(f"ID: {current.student_id} | Name: {current.student_name} | GPA: {current.gpa}")
            current = current.next

    def filter_high_gpa(self):
        print("--- GPA > 80 olanlar ---")
        current = self.head
        while current:
            if current.gpa > 80:
                print(f"{current.student_name} (GPA: {current.gpa})")
            current = current.next

    def search_by_name(self, name):
        current = self.head
        while current:
            if current.student_name.lower() == name.lower():
                print(f"Tapıldı: ID: {current.student_id}, Name: {current.student_name}, GPA: {current.gpa}")
                return
            current = current.next
        print("Tələbə tapılmadı.")

    def count_students(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        print(f"Ümumi tələbə sayı: {count}")
        return count


if __name__ == "__main__":
    print("=== Task 1: Node sinfinin yaradılması ===")
    node1 = Node(15)
    print(f"Data: {node1.data}, Next: {node1.next}\n")

    print("=== Task 2: Siyahının sonuna element əlavə etmək ===")
    ll = LinkedList()
    for val in [10, 20, 30, 40]:
        ll.append(val)
    ll.display()
    print()

    print("=== Task 3: Siyahının əvvəlinə element əlavə etmək ===")
    ll3 = LinkedList()
    for val in [20, 30, 40]:
        ll3.append(val)
    ll3.prepend(10)
    ll3.display()
    print()

    print("=== Task 4: Verilmiş elementdən sonra əlavə etmək ===")
    ll4 = LinkedList()
    for val in [10, 20, 40]:
        ll4.append(val)
    ll4.insert_after(20, 30)
    ll4.display()
    print()

    print("=== Task 5: Element silmək ===")
    ll5 = LinkedList()
    for val in [10, 20, 30, 40, 50]:
        ll5.append(val)
    ll5.delete_node(30)
    ll5.display()
    print()

    print("=== Task 6: Axtarış ===")
    ll6 = LinkedList()
    for val in [10, 20, 30, 40]:
        ll6.append(val)
    ll6.search(30)
    ll6.search(99)
    print()

    print("=== Task 7: Uzunluğun hesablanması ===")
    ll7 = LinkedList()
    for val in [11, 22, 33, 44, 55]:
        ll7.append(val)
    ll7.length()
    print()

    print("=== Task 8: Maksimum və minimum element ===")
    ll8 = LinkedList()
    for val in [23, 8, 91, 15, 42]:
        ll8.append(val)
    ll8.find_min_max()
    print()

    print("=== Task 9: Siyahını tərs çevirmək ===")
    ll9 = LinkedList()
    for val in [10, 20, 30, 40, 50]:
        ll9.append(val)
    ll9.reverse()
    ll9.display()
    print()

    print("=== Task 10: Tələbə qeydiyyat sistemi (Challenge) ===")
    sr = StudentRegistry()
    sr.add_student(1, "Ali Aliyev", 85)
    sr.add_student(2, "Leyla Mammadova", 78)
    sr.add_student(3, "Murad Huseynov", 92)
    sr.filter_high_gpa()
    sr.count_students()
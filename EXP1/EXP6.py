class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at Beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert at End
    def insert_at_end(self, data):
        new_node = Node(data)
        new_node.next = None
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    # Delete from Beginning
    def delete_from_beginning(self):
        if self.head is None:
            print("List is empty")
            return
        self.head = self.head.next

    # Delete from End
    def delete_from_end(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            self.head = None
            return
        current = self.head
        while current.next.next is not None:
            current = current.next
        current.next = None

    # Search
    def search(self, key):
        current = self.head
        while current is not None:
            if current.data == key:
                print("Element found")
                return
            current = current.next
        print("Element not found")

    # Display / Traverse
    def display(self):
        if self.head is None:
            print("List is empty")
            return
        current = self.head
        elements = []
        while current is not None:
            elements.append(str(current.data))
            current = current.next
        elements.append("None")
        print(" -> ".join(elements))


# Driver code with menu-driven interface matching the expected output
if __name__ == "__main__":
    sll = SinglyLinkedList()
    
    while True:
        print("\n--- SINGLY LINKED LIST ---")
        print("1. Insert at Beginning")
        print("2. Insert at End")
        print("3. Delete from Beginning")
        print("4. Delete from End")
        print("5. Search")
        print("6. Display")
        print("7. Exit")
        
        try:
            choice = int(input("\nEnter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 7.")
            continue

        if choice == 1:
            data = int(input("Enter data: "))
            sll.insert_at_beginning(data)
        elif choice == 2:
            data = int(input("Enter data: "))
            sll.insert_at_end(data)
        elif choice == 3:
            sll.delete_from_beginning()
        elif choice == 4:
            sll.delete_from_end()
        elif choice == 5:
            key = int(input("Enter data to search: "))
            sll.search(key)
        elif choice == 6:
            sll.display()
        elif choice == 7:
            print("Exit")
            break
        else:
            print("Invalid choice! Please choose a valid option.")

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at Beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    # Insert at End
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next is not None:
            last = last.next
        last.next = new_node
        new_node.prev = last

    # Delete from Beginning
    def delete_from_beginning(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            self.head = None
            return
        self.head = self.head.next
        self.head.prev = None

    # Delete from End
    def delete_from_end(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            self.head = None
            return
        last = self.head
        while last.next is not None:
            last = last.next
        last.prev.next = None

    # Search for an Element
    def search(self, key):
        current = self.head
        while current is not None:
            if current.data == key:
                print("Element found")
                return
            current = current.next
        print("Element not found")

    # Display Forward
    def display_forward(self):
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

    # Display Backward
    def display_backward(self):
        if self.head is None:
            print("List is empty")
            return
        last = self.head
        while last.next is not None:
            last = last.next
        elements = []
        while last is not None:
            elements.append(str(last.data))
            last = last.prev
        elements.append("None")
        print(" -> ".join(elements))


# Driver code with menu-driven interface
if __name__ == "__main__":
    dll = DoublyLinkedList()
    
    while True:
        print("\n--- DOUBLY LINKED LIST ---")
        print("1. Insert at Beginning")
        print("2. Insert at End")
        print("3. Delete from Beginning")
        print("4. Delete from End")
        print("5. Search")
        print("6. Display Forward")
        print("7. Display Backward")
        print("8. Exit")
        
        try:
            choice = int(input("\nEnter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 8.")
            continue

        if choice == 1:
            data = int(input("Enter data: "))
            dll.insert_at_beginning(data)
        elif choice == 2:
            data = int(input("Enter data: "))
            dll.insert_at_end(data)
        elif choice == 3:
            dll.delete_from_beginning()
        elif choice == 4:
            dll.delete_from_end()
        elif choice == 5:
            key = int(input("Enter data to search: "))
            dll.search(key)
        elif choice == 6:
            dll.display_forward()
        elif choice == 7:
            dll.display_backward()
        elif choice == 8:
            print("Exiting program.")
            break
        else:
            print("Invalid choice! Please choose a valid option.")

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Insert at Beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            last = self.head
            while last.next != self.head:
                last = last.next
            new_node.next = self.head
            last.next = new_node
            self.head = new_node

    # Insert at End
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            last = self.head
            while last.next != self.head:
                last = last.next
            last.next = new_node
            new_node.next = self.head

    # Delete from Beginning
    def delete_from_beginning(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next == self.head:
            self.head = None
        else:
            last = self.head
            while last.next != self.head:
                last = last.next
            self.head = self.head.next
            last.next = self.head

    # Delete from End
    def delete_from_end(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next == self.head:
            self.head = None
        else:
            current = self.head
            while current.next.next != self.head:
                current = current.next
            current.next = self.head

    # Search
    def search(self, key):
        if self.head is None:
            print("Element not found")
            return
        current = self.head
        found = False
        while True:
            if current.data == key:
                found = True
                break
            current = current.next
            if current == self.head:
                break
        if found:
            print("Element found")
        else:
            print("Element not found")

    # Display
    def display(self):
        if self.head is None:
            print("List is empty")
            return
        current = self.head
        elements = []
        while True:
            elements.append(str(current.data))
            current = current.next
            if current == self.head:
                break
        elements.append("(back to head)")
        print(" -> ".join(elements))


# Driver code with menu-driven interface matching the expected output
if __name__ == "__main__":
    cll = CircularLinkedList()
    
    while True:
        print("\n--- CIRCULAR LINKED LIST ---")
        print("1. Insert at Beginning")
        print("2. Insert at End")
        print("3. Delete from Beginning")
        print("4. Delete from End")
        print("5. Search")
        print("6. Display")
        print("7. Exit")
        
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 7.")
            continue

        if choice == 1:
            data = int(input("\nEnter data: "))
            cll.insert_at_beginning(data)
        elif choice == 2:
            data = int(input("\nEnter data: "))
            cll.insert_at_end(data)
        elif choice == 3:
            cll.delete_from_beginning()
        elif choice == 4:
            cll.delete_from_end()
        elif choice == 5:
            key = int(input("\nEnter element to search: "))
            cll.search(key)
        elif choice == 6:
            print()
            cll.display()
        elif choice == 7:
            print("\nExit")
            break
        else:
            print("Invalid choice! Please choose a valid option.")

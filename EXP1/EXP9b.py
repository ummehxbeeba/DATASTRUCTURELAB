class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    # Enqueue operation
    def enqueue(self, item):
        new_node = Node(item)
        if self.front is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        print("Item inserted successfully")

    # Dequeue operation
    def dequeue(self):
        if self.front is None:
            print("Queue Underflow")
            return
        item = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        print(f"Deleted item is {item}")

    # Peek operation
    def peek(self):
        if self.front is None:
            print("Queue Underflow")
            return
        print(f"Front item is {self.front.data}")

    # Display operation
    def display(self):
        if self.front is None:
            print("Queue Underflow")
            return
        print("Queue elements:")
        temp = self.front
        elements = []
        while temp is not None:
            elements.append(str(temp.data))
            temp = temp.next
        print(" ".join(elements))


# Driver code with menu-driven interface matching the expected output
if __name__ == "__main__":
    queue = Queue()
    
    while True:
        print("\n--- QUEUE USING LINKED LIST ---")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek")
        print("4. Display")
        print("5. Exit")
        
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 5.")
            continue

        if choice == 1:
            item = int(input("Enter item to insert: "))
            queue.enqueue(item)
        elif choice == 2:
            queue.dequeue()
        elif choice == 3:
            queue.peek()
        elif choice == 4:
            queue.display()
        elif choice == 5:
            print("Exit")
            break
        else:
            print("Invalid choice! Please choose a valid option.")

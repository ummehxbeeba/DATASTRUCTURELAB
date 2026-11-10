class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    # Push operation
    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        print("Item pushed successfully")

    # Pop operation
    def pop(self):
        if self.top is None:
            print("Stack Underflow")
            return
        popped_item = self.top.data
        self.top = self.top.next
        print(f"Popped item is {popped_item}")

    # Peek operation
    def peek(self):
        if self.top is None:
            print("Stack Underflow")
            return
        print(f"Top item is {self.top.data}")

    # Display operation
    def display(self):
        if self.top is None:
            print("Stack Underflow")
            return
        print("Stack elements:")
        temp = self.top
        while temp is not None:
            print(temp.data)
            temp = temp.next


# Driver code with menu-driven interface matching the expected output
if __name__ == "__main__":
    stack = Stack()
    
    while True:
        print("\n--- STACK USING LINKED LIST ---")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Display")
        print("5. Exit")
        
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 5.")
            continue

        if choice == 1:
            item = int(input("Enter item to push: "))
            stack.push(item)
        elif choice == 2:
            stack.pop()
        elif choice == 3:
            stack.peek()
        elif choice == 4:
            stack.display()
        elif choice == 5:
            print("Exit")
            break
        else:
            print("Invalid choice! Please choose a valid option.")

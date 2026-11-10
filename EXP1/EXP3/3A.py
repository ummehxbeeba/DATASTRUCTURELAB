class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = []
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.capacity - 1

    def push(self, item):
        print("\nPUSH")
        if self.is_full():
            print("Stack Overflow")
            return
        self.top += 1
        if len(self.stack) <= self.top:
            self.stack.append(item)
        else:
            self.stack[self.top] = item
        print("Item pushed successfully")
        self.display_stack_elements()

    def pop(self):
        print("\nPOP")
        if self.is_empty():
            print("Stack Underflow")
            return -1
        item = self.stack[self.top]
        self.top -= 1
        print(f"Deleted element = {item}")
        return item

    def peek(self):
        print("\nPEEK")
        if self.is_empty():
            print("Stack Underflow")
            return None
        return self.stack[self.top]

    def display(self):
        print("\nDISPLAY")
        if self.is_empty():
            print("Stack Underflow")
            return
        for i in range(self.top, -1, -1):
            print(self.stack[i])

    def display_stack_elements(self):
        for i in range(self.top + 1):
            print(self.stack[i], end=" ")
        print()


if __name__ == "__main__":
    print("STack")
    try:
        capacity = int(input("enter capacity of Stack"))
    except ValueError:
        capacity = 5

    s = Stack(capacity)
    print(f"Stack with capacity {capacity} created")

    while True:
        print("\n1.Push")
        print("2.Pop")
        print("3.Peek")
        print("4.Display")
        print("5.Exit")
        
        try:
            choice = int(input("enter your Choice"))
        except ValueError:
            print("Invalid choice!")
            continue

        if choice == 1:
            try:
                item = int(input("Enter item to push into stack"))
                s.push(item)
            except ValueError:
                print("Invalid item!")
        elif choice == 2:
            s.pop()
        elif choice == 3:
            val = s.peek()
            if val is not None:
                print(f"Peek = {val}\nThe element {val} is not removed.")
        elif choice == 4:
            s.display()
        elif choice == 5:
            print("Exit the program")
            break
        else:
            print("Invalid choice!")

        cont = input("Do you want to continue y/n?: ").strip().lower()
        if cont == 'n':
            print("Exit the program")
            break

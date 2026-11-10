class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def enqueue(self, item):
        print("\nENQUEUE")
        if self.is_full():
            print("Queue Overflow")
            return
        
        if self.is_empty():
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.capacity
            
        self.queue[self.rear] = item
        print("Item inserted successfully")

    def dequeue(self):
        print("\nDEQUEUE")
        if self.is_empty():
            print("Queue Underflow")
            return -1
        
        item = self.queue[self.front]
        
        if self.front == self.rear:
            # Queue has only one element, reset after deletion
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
            
        print(f"Deleted item is {item}")
        return item

    def peek(self):
        print("\nPEEK")
        if self.is_empty():
            print("Queue Underflow")
            return -1
        
        front_item = self.queue[self.front]
        print(f"Front item is {front_item}")
        return front_item

    def display(self):
        print("\nDISPLAY")
        if self.is_empty():
            print("Queue Underflow")
            return
        
        print("Queue elements:")
        elements = []
        i = self.front
        while True:
            elements.append(str(self.queue[i]))
            if i == self.rear:
                break
            i = (i + 1) % self.capacity
        print(" ".join(elements))


# Driver code with menu-driven interface matching the expected output format
if __name__ == "__main__":
    print("CIRCULAR QUEUE")
    try:
        capacity = int(input("Enter capacity of Circular Queue: "))
    except ValueError:
        capacity = 5  # Default fallback capacity

    cq = CircularQueue(capacity)
    print(f"\nCircular Queue with capacity {capacity} created")

    while True:
        print("\n1. Enqueue")
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
            try:
                item = int(input("Enter item to insert: "))
                cq.enqueue(item)
            except ValueError:
                print("Invalid item! Please enter an integer.")
        elif choice == 2:
            cq.dequeue()
        elif choice == 3:
            cq.peek()
        elif choice == 4:
            cq.display()
        elif choice == 5:
            print("\nExit")
            break
        else:
            print("Invalid choice! Please choose a valid option.")

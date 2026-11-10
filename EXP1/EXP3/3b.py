class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.front == -1 or self.front > self.rear

    def is_full(self):
        return self.rear == self.capacity - 1

    def enqueue(self, item):
        print("\nENQUEUE")
        if self.is_full():
            print("Queue Overflow")
            return
        
        self.rear += 1
        self.queue[self.rear] = item
        if self.front == -1:
            self.front = 0
            
        print("Item inserted successfully")
        self.display_queue_line()

    def dequeue(self):
        print("\nDEQUEUE")
        if self.is_empty():
            print("Queue Underflow")
            return -1
        
        item = self.queue[self.front]
        self.front += 1
        if self.front > self.rear:
            self.front = -1
            self.rear = -1
            
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
        for i in range(self.front, self.rear + 1):
            print(self.queue[i], end=" ")
        print()

    def display_queue_line(self):
        print("Queue elements:")
        for i in range(self.front, self.rear + 1):
            print(self.queue[i], end=" ")
        print()


if __name__ == "__main__":
    print("QUEUE")
    try:
        capacity = int(input("Enter capacity of Queue: "))
    except ValueError:
        capacity = 5

    q = Queue(capacity)
    print(f"Queue with capacity {capacity} created")

    while True:
        print("\n1. Enqueue")
        print("2. Dequeue")
        print("3. Peek")
        print("4. Display")
        print("5. Exit")
        
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid choice!")
            continue

        if choice == 1:
            try:
                item = int(input("Enter item to insert into queue: "))
                q.enqueue(item)
            except ValueError:
                print("Invalid item!")
        elif choice == 2:
            q.dequeue()
        elif choice == 3:
            q.peek()
        elif choice == 4:
            q.display()
        elif choice == 5:
            print("Exit")
            break
        else:
            print("Invalid choice!")

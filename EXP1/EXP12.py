class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    # Get height of a node
    def _height(self, root):
        if not root:
            return 0
        return root.height

    # Get balance factor of a node
    def _get_balance(self, root):
        if not root:
            return 0
        return self._height(root.left) - self._height(root.right)

    # Right Rotation (LL Case)
    def _right_rotate(self, y):
        x = y.left
        T2 = x.right

        # Perform rotation
        x.right = y
        y.left = T2

        # Update heights
        y.height = max(self._height(y.left), self._height(y.right)) + 1
        x.height = max(self._height(x.left), self._height(x.right)) + 1

        return x

    # Left Rotation (RR Case)
    def _left_rotate(self, x):
        y = x.right
        T2 = y.left

        # Perform rotation
        y.left = x
        x.right = T2

        # Update heights
        x.height = max(self._height(x.left), self._height(x.right)) + 1
        y.height = max(self._height(y.left), self._height(y.right)) + 1

        return y

    # Insert operation
    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)
        print("Element inserted successfully")

    def _insert_recursive(self, root, key):
        # 1. Perform standard BST insertion
        if not root:
            return Node(key)
        elif key < root.val:
            root.left = self._insert_recursive(root.left, key)
        elif key > root.val:
            root.right = self._insert_recursive(root.right, key)
        else:
            return root  # Duplicate keys not allowed

        # 2. Update height of this root node
        root.height = 1 + max(self._height(root.left), self._height(root.right))

        # 3. Get the balance factor to check if this node became unbalanced
        balance = self._get_balance(root)

        # 4. If unbalanced, apply the 4 rotations

        # LL Case (Right Rotation)
        if balance > 1 and key < root.left.val:
            return self._right_rotate(root)

        # RR Case (Left Rotation)
        if balance < -1 and key > root.right.val:
            return self._left_rotate(root)

        # LR Case (Left Rotation then Right Rotation)
        if balance > 1 and key > root.left.val:
            root.left = self._left_rotate(root.left)
            return self._right_rotate(root)

        # RL Case (Right Rotation then Left Rotation)
        if balance < -1 and key < root.right.val:
            root.right = self._right_rotate(root.right)
            return self._left_rotate(root)

        return root

    # Search operation
    def search(self, key):
        if self._search_recursive(self.root, key):
            print("Element found")
        else:
            print("Element not found")

    def _search_recursive(self, root, key):
        if not root or root.val == key:
            return root
        if key < root.val:
            return self._search_recursive(root.left, key)
        return self._search_recursive(root.right, key)

    # Inorder Traversal Display
    def display_inorder(self):
        elements = []
        self._inorder_recursive(self.root, elements)
        print("Inorder Traversal:")
        print(" ".join(map(str, elements)))

    def _inorder_recursive(self, root, elements):
        if root:
            self._inorder_recursive(root.left, elements)
            elements.append(root.val)
            self._inorder_recursive(root.right, elements)


# Driver code with menu-driven interface matching the expected output
if __name__ == "__main__":
    avl = AVLTree()
    
    while True:
        print("\n--- AVL TREE ---")
        print("1. Insert")
        print("2. Search")
        print("3. Display Inorder")
        print("4. Exit")
        
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            try:
                val = int(input("Enter value to insert: "))
                avl.insert(val)
            except ValueError:
                print("Invalid value! Please enter an integer.")
        elif choice == 2:
            try:
                val = int(input("Enter value to search: "))
                avl.search(val)
            except ValueError:
                print("Invalid value! Please enter an integer.")
        elif choice == 3:
            avl.display_inorder()
        elif choice == 4:
            print("Exit")
            break
        else:
            print("Invalid choice! Please choose a valid option.")

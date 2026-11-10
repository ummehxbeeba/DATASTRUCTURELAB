class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Insertion
    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)
        print("Element inserted successfully")

    def _insert_recursive(self, root, key):
        if root is None:
            return Node(key)
        if key < root.val:
            root.left = self._insert_recursive(root.left, key)
        elif key > root.val:
            root.right = self._insert_recursive(root.right, key)
        return root

    # Search
    def search(self, key):
        if self._search_recursive(self.root, key):
            print("Element found")
        else:
            print("Element not found")

    def _search_recursive(self, root, key):
        if root is None or root.val == key:
            return root
        if key < root.val:
            return self._search_recursive(root.left, key)
        return self._search_recursive(root.right, key)

    # Deletion
    def delete(self, key):
        # Check if the element exists first to print the appropriate message
        if self._search_recursive(self.root, key) is None:
            print("Element not found")
            return
        self.root = self._delete_recursive(self.root, key)
        print("Element deleted successfully")

    def _delete_recursive(self, root, key):
        if root is None:
            return root

        if key < root.val:
            root.left = self._delete_recursive(root.left, key)
        elif key > root.val:
            root.right = self._delete_recursive(root.right, key)
        else:
            # Case 1: No child or only one child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Case 2: Two children -> Get the inorder successor (min in the right subtree)
            temp = self._min_value_node(root.right)
            root.val = temp.val
            root.right = self._delete_recursive(root.right, temp.val)

        return root

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

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
    bst = BinarySearchTree()
    
    while True:
        print("\n--- BINARY SEARCH TREE ---")
        print("1. Insertion")
        print("2. Deletion")
        print("3. Search")
        print("4. Display (Inorder)")
        print("5. Exit")
        
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 5.")
            continue

        if choice == 1:
            val = int(input("Enter value to insert: "))
            bst.insert(val)
        elif choice == 2:
            val = int(input("Enter value to delete: "))
            bst.delete(val)
        elif choice == 3:
            val = int(input("Enter value to search: "))
            bst.search(val)
        elif choice == 4:
            bst.display_inorder()
        elif choice == 5:
            print("Exit")
            break
        else:
            print("Invalid choice! Please choose a valid option.")

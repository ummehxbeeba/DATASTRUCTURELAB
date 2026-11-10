class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    # Inorder Traversal: Left -> Root -> Right
    def inorder(self, root, result):
        if root:
            self.inorder(root.left, result)
            result.append(str(root.data))
            self.inorder(root.right, result)

    # Preorder Traversal: Root -> Left -> Right
    def preorder(self, root, result):
        if root:
            result.append(str(root.data))
            self.preorder(root.left, result)
            self.preorder(root.right, result)

    # Postorder Traversal: Left -> Right -> Root
    def postorder(self, root, result):
        if root:
            self.postorder(root.left, result)
            self.postorder(root.right, result)
            result.append(str(root.data))

    def display_traversals(self):
        # Inorder
        inorder_result = []
        self.inorder(self.root, inorder_result)
        print(f"• Inorder (Left → Root → Right): {' '.join(inorder_result)}")

        # Preorder
        preorder_result = []
        self.preorder(self.root, preorder_result)
        print(f"• Preorder (Root → Left → Right): {' '.join(preorder_result)}")

        # Postorder
        postorder_result = []
        self.postorder(self.root, postorder_result)
        print(f"• Postorder (Left → Right → Root): {' '.join(postorder_result)}")


# Driver code constructing the example binary tree
if __name__ == "__main__":
    # Constructing the tree:
    #             1
    #           /   \
    #          2     3
    #         / \   / \
    #        4   5 6   7

    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)

    # Perform and display traversals matching expected output
    tree.display_traversals()

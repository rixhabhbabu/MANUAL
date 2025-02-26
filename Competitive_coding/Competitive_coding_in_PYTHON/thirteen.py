class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def pre_order_traversal(root):
    if root:
        print(root.data, end=" ")  # Visit root first
        pre_order_traversal(root.left)  # Then visit left subtree
        pre_order_traversal(root.right)  # Then visit right subtree

def in_order_traversal(root):
    if root:
        in_order_traversal(root.left)  # Visit left subtree first
        print(root.data, end=" ")  # Then visit root
        in_order_traversal(root.right)  # Then visit right subtree

def post_order_traversal(root):
    if root:
        post_order_traversal(root.left)  # Visit left subtree first
        post_order_traversal(root.right)  # Then visit right subtree
        print(root.data, end=" ")  # Then visit root

if __name__ == "__main__":
    # Create a sample binary tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    
    # Perform tree traversals
    print("Pre-order traversal:", end=" ")
    pre_order_traversal(root)
    print()
    
    print("In-order traversal:", end=" ")
    in_order_traversal(root)
    print()
    
    print("Post-order traversal:", end=" ")
    post_order_traversal(root)
    print()

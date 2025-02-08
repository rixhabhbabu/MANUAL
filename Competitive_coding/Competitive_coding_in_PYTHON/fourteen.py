# BST class representing a node in the Binary Search Tree
class BST:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Function to insert a new node into the BST
def insert(root, val):
    if root is None:
        return BST(val)
    
    if root.data < val:
        root.right = insert(root.right, val)
    else:
        root.left = insert(root.left, val)
    
    return root

# Function to perform an inorder traversal of the BST
def inorder(root):
    if root is None:
        return
    
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)

# Main method to create a sample BST and perform inorder traversal
if __name__ == "__main__":
    root = None
    root = insert(root, 80)
    root = insert(root, 60)
    root = insert(root, 90)
    root = insert(root, 10)
    root = insert(root, 70)
    root = insert(root, 85)
    root = insert(root, 110)

    print("In-order traversal of the BST:")
    inorder(root)
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def are_mirror(root1, root2):
    # Base case: Both trees are empty
    if root1 is None and root2 is None:
        return True
    # One tree is empty and the other is not
    if root1 is None or root2 is None:
        return False
    # Check if root data matches and subtrees are mirrors
    return (root1.data == root2.data and
            are_mirror(root1.left, root2.right) and
            are_mirror(root1.right, root2.left))

if __name__ == "__main__":
    # Create mirrored trees
    root1 = Node(1)
    root1.left = Node(2)
    root1.right = Node(3)
    root1.left.left = Node(4)
    root1.left.right = Node(5)

    root2 = Node(1)
    root2.left = Node(3)
    root2.right = Node(2)
    root2.right.left = Node(5)
    root2.right.right = Node(4)

    # Check if the trees are mirror images
    if are_mirror(root1, root2):
        print("Given trees are mirrored trees.")
    else:
        print("Given trees are not mirrored trees.")

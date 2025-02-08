# Node class representing a node in the tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Function to find the Lowest Common Ancestor (LCA) of two nodes
def findLCA(root, n1, n2):
    # Base case: Empty tree or root matches one of the nodes
    if root is None or root.data == n1 or root.data == n2:
        return root

    # Recursively search for n1 and n2 in left and right subtrees
    leftLCA = findLCA(root.left, n1, n2)
    rightLCA = findLCA(root.right, n1, n2)

    # If both left and right subtrees found a node, then root is LCA
    if leftLCA is not None and rightLCA is not None:
        return root

    # Return the only node found (if one is in left and the other in right)
    return leftLCA if leftLCA is not None else rightLCA

# Main method to create a sample tree and find LCA
if __name__ == "__main__":
    # Create a sample binary tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    # Find LCA of nodes 4 and 7
    n1, n2 = 4, 7
    lca = findLCA(root, n1, n2)

    if lca is not None:
        print(f"LCA of {n1} and {n2} is: {lca.data}")
    else:
        print("LCA not found.")
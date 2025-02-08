class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def max_depth(root):
    if root is None:
        return 0  # Empty tree has depth 0
    
    # Recursively find depths of left and right subtrees
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)
    
    # Return the larger depth + 1 (for the current node)
    return max(left_depth, right_depth) + 1

if __name__ == "__main__":
    # Create a sample binary tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    
    # Calculate and print the depth of the tree
    depth = max_depth(root)
    print("Depth of the tree:", depth)

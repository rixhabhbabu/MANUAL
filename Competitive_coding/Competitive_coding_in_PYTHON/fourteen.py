class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BoundaryTraversal:
    def boundary_traversal(self, root):
        if not root:
            return

        boundary = []
        boundary.append(root.val)  # Step 1: Add the root

        # Step 2: Add left boundary (excluding leaf nodes)
        self.add_left_boundary(root.left, boundary)
        
        # Step 3: Add leaf nodes
        self.add_leaves(root, boundary)
        
        # Step 4: Add right boundary (excluding leaf nodes)
        self.add_right_boundary(root.right, boundary)
        
        # Print the boundary traversal
        print(" ".join(map(str, boundary)))

    def add_left_boundary(self, node, boundary):
        while node:
            if node.left or node.right:  # Exclude leaf nodes
                boundary.append(node.val)
            node = node.left if node.left else node.right  # Move to the leftmost child

    def add_leaves(self, node, boundary):
        if not node:
            return
        if not node.left and not node.right:
            boundary.append(node.val)
        self.add_leaves(node.left, boundary)
        self.add_leaves(node.right, boundary)

    def add_right_boundary(self, node, boundary):
        temp = []
        while node:
            if node.left or node.right:  # Exclude leaf nodes
                temp.append(node.val)
            node = node.right if node.right else node.left  # Move to the rightmost child
        boundary.extend(temp[::-1])  # Add right boundary in reverse order

# Main method to test the boundary traversal
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    root.left.left.left = TreeNode(8)

    traversal = BoundaryTraversal()
    print("Boundary Traversal of the binary search tree:")
    traversal.boundary_traversal(root)

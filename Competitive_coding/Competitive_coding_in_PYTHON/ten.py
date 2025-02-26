# TreeNode class representing a node in the Binary Search Tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Class to validate a BST
class ValidateBST:
    def isValidBST(self, root):
        # Helper function to recursively validate the BST
        def isValidBSTHelper(node, min_val, max_val):
            # Base case: an empty node is a valid BST
            if node is None:
                return True

            # Check if the current node's value is within the valid range
            if node.val <= min_val or node.val >= max_val:
                return False

            # Recursively check the left and right subtrees
            return (isValidBSTHelper(node.left, min_val, node.val) and
                    isValidBSTHelper(node.right, node.val, max_val))

        # Initial call to the helper function with the root and the full range
        return isValidBSTHelper(root, float('-inf'), float('inf'))

# Main method to test the BST validation
if __name__ == "__main__":
    # Example usage:
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)

    validator = ValidateBST()
    print(validator.isValidBST(root))  # Output: True

    # Example of an invalid BST
    invalidRoot = TreeNode(5)
    invalidRoot.left = TreeNode(1)
    invalidRoot.right = TreeNode(4)
    invalidRoot.right.left = TreeNode(3)
    invalidRoot.right.right = TreeNode(6)

    print(validator.isValidBST(invalidRoot))  # Output: False
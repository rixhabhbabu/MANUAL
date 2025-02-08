from collections import deque

# Definition for a binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class LevelOrderTraversal:
    def level_order(self, root):
        if not root:
            return  # If the tree is empty, return
        
        queue = deque([root])  # Create a queue and enqueue the root node
        
        while queue:
            current_node = queue.popleft()  # Dequeue the front node
            print(current_node.val, end=" ")  # Process the node (print its value)
            
            # Enqueue left child
            if current_node.left:
                queue.append(current_node.left)
            
            # Enqueue right child
            if current_node.right:
                queue.append(current_node.right)

# Main method to test the level order traversal
if __name__ == "__main__":
    # Create a sample binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    traversal = LevelOrderTraversal()
    print("Level Order Traversal of the binary tree:")
    traversal.level_order(root)  # Perform level order traversal
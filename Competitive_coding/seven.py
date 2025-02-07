class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def merge_two_lists(l1, l2):
    dummy = Node(0)  # Create a dummy node to simplify the merging process
    l3 = dummy  # This will be the tail of the merged list

    # Traverse both lists and merge them in sorted order
    while l1 and l2:
        if l1.data < l2.data:
            l3.next = l1  # Link the smaller node to the merged list
            l1 = l1.next  # Move to the next node in l1
        else:
            l3.next = l2  # Link the smaller node to the merged list
            l2 = l2.next  # Move to the next node in l2
        l3 = l3.next  # Move the tail pointer forward

    # If one of the lists is not exhausted, link the remaining nodes
    l3.next = l1 if l1 else l2

    return dummy.next  # Return the merged list, skipping the dummy node

# Function to print linked list
def print_list(node):
    while node:
        print(node.data, end=" -> " if node.next else "\n")
        node = node.next

if __name__ == "__main__":
    # Create first sorted linked list: 1 -> 2 -> 4
    l1 = Node(1)
    l1.next = Node(2)
    l1.next.next = Node(4)

    # Create second sorted linked list: 1 -> 3 -> 4
    l2 = Node(1)
    l2.next = Node(3)
    l2.next.next = Node(4)

    # Merge the two lists
    merged_list = merge_two_lists(l1, l2)

    # Print the merged list
    print_list(merged_list)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def find_merge_point(l1, l2):
    while l1 and l2:
        if l1.data < l2.data:
            l1 = l1.next
        elif l1.data > l2.data:
            l2 = l2.next
        else:
            return l1  # Merge point found
    return None  # No merge point found

def print_result(merge_point):
    if merge_point:
        print("Merge Point:", merge_point.data)
    else:
        print("No Merge Point found.")

if __name__ == "__main__":
    # Create the intersecting node
    intersect_node = Node(8)
    
    # Create the first linked list: 1 -> 3 -> 5 -> 8
    l1 = Node(1)
    l1.next = Node(3)
    l1.next.next = Node(5)
    l1.next.next.next = intersect_node  # Link to the intersecting node
    
    # Create the second linked list: 2 -> 4 -> 8
    l2 = Node(2)
    l2.next = Node(4)
    l2.next.next = intersect_node  # Link to the same intersecting node
    
    # Find the merge point
    merge_point = find_merge_point(l1, l2)
    
    # Print the result
    print_result(merge_point)

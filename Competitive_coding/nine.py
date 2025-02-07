class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def swap(head):
    l1 = head
    while l1 and l1.next:
        l1.data, l1.next.data = l1.next.data, l1.data  # Swap data
        l1 = l1.next.next  # Move to the next pair
    return head

def address_swap(head):
    dummy = Node(-1)
    dummy.next = head
    point = dummy
    
    while point.next and point.next.next:
        swap1 = point.next
        swap2 = point.next.next
        
        # Swapping the nodes
        swap1.next = swap2.next
        swap2.next = swap1
        point.next = swap2
        
        # Move the pointer forward
        point = swap1
    
    return dummy.next  # Return the new head of the list

def print_list(head):
    while head:
        print(head.data, end=" -> " if head.next else "\n")
        head = head.next

if __name__ == "__main__":
    l1 = Node(3)
    l1.next = Node(5)
    l1.next.next = Node(4)
    l1.next.next.next = Node(7)
    
    head = address_swap(l1)  # Swap nodes in pairs
    print_list(head)

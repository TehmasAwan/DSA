class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_sort_linked_list(head):
    if not head or not head.next:
        return head

    mid = find_middle(head)
    left_half = head
    right_half = mid.next
    mid.next = None

    left_sorted = merge_sort_linked_list(left_half)
    right_sorted = merge_sort_linked_list(right_half)

    return merge(left_sorted, right_sorted)

def find_middle(head):
    if not head:
        return None

    slow = head
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    return slow

def merge(left, right):
    dummy = ListNode()
    current = dummy

    while left and right:
        if left.val < right.val:
            current.next = left
            left = left.next
        else:
            current.next = right
            right = right.next
        current = current.next

    current.next = left or right

    return dummy.next

def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Example usage:
# Create a sample linked list
head = ListNode(3, ListNode(1, ListNode(4, ListNode(2, ListNode(5)))))
print("Original linked list:")
print_linked_list(head)

sorted_head = merge_sort_linked_list(head)
print("Sorted linked list:")
print_linked_list(sorted_head)

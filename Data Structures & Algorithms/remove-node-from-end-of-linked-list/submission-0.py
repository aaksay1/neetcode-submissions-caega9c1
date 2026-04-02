# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0

        curr = head
        while(curr):
            curr = curr.next
            size += 1
        
        to_remove = size - n

        curr = head
        dummy = ListNode(0)
        dummy.next = curr
        curr_node = 0

        if to_remove == 0:
            return dummy.next.next
        while curr:
            if curr_node == to_remove - 1:
                curr.next = curr.next.next
            else:
                curr = curr.next
            curr_node += 1
        
        return dummy.next

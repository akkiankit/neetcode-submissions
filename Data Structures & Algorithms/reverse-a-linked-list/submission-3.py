# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        # for reversal we need revese the pointer of each node
        while curr:
            nex = curr.next # store the all the next element
            # assign next element to 
            curr.next = prev
            prev = curr
            curr = nex
        return prev

        
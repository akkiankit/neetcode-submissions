# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # two pass aprroach
        # counting the lenth of linked list
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        dummy = ListNode(0, head)
        prev = dummy
        for _ in range(length - n):
            prev = prev.next
        
        prev.next = prev.next.next

        return dummy.next 



        
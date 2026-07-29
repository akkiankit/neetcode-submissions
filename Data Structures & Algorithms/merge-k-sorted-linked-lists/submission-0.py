# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        res = ListNode(0)
        tail = res
        counter = 0
        for listnodes in lists:
            curr = listnodes
            while curr:
                heapq.heappush(heap, (curr.val, counter, curr))
                curr = curr.next
                counter += 1
        
        while heap:
            value, counter, pointer = heapq.heappop(heap)
            # tail.val = value
            tail.next = pointer
            tail = tail.next
        tail.next = None
        
        return res.next

    
        
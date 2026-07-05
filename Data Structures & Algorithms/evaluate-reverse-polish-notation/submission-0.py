class DoblyLinkedList:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Doubly Linked List:
        head = DoblyLinkedList(tokens[0])
        curr = head
        for i in range(1, len(tokens)):
            curr.next = DoblyLinkedList(tokens[i], prev=curr)
            curr = curr.next
        
        while head is not None:
            if head.val in "+-*/":
                l = int(head.prev.prev.val)
                r = int(head.prev.val)
                if head.val == '+':
                    res = l + r
                elif head.val == '-':
                    res = l - r
                elif head.val == '*':
                    res = l * r
                else:
                    res = int(l / r)

                head.val = str(res)
                head.prev = head.prev.prev.prev
                if head.prev is not None:
                    head.prev.next = head

            ans = int(head.val)
            head = head.next

        return ans

        # while len(tokens) > 1:
        #     for i in range(len(tokens)):
        #         if tokens[i] in "+-*/":
        #             a = tokens[i-2]
        #             b = tokens[i-1]
        #             if tokens[i] == '+':
        #                 res = a + b
        #             elif tokens[i] == '-':
        #                 res = a - b
        #             elif tokens[i] == '*':
        #                 res = a * b
        #             elif tokens[i] == '/':
        #                 res = a / b
        #             tokens = tokens[:i-2] + [str(res)] + tokens[i+1:]
        #         break
        # return int(tokens[0])
        
                    
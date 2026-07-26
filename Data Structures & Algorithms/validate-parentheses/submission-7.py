class Solution:
    def isValid(self, s: str) -> bool:
        
        closedToOpen = {"}":"{", "]":"[", ")": "("}
        stack = []
        for br in s:
            if br in closedToOpen:
                if stack and stack[-1] == closedToOpen[br]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(br)
        return True if not stack else False


        
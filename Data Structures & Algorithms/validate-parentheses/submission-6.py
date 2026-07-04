class Solution:
    def isValid(self, s: str) -> bool:
        # stack - here we will track the opening brackets - stack is also a kind of list 
        # only in python - in this approach try to use a hashmap to track the relationship what i mean is
        # if s is starting with }, ], ) then it will always we invalid so we need hasmap to map it
        closeToOpen = {')': '(', ']' : '[', '}': '{'}
        stack = []
        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False




        # # Brute force - we need to replace the valid pair with '' 
        # while '()' in s or '{}' in s or '[]' in s:
        #     s = s.replace('[]','')
        #     s = s.replace('()', '')
        #     s = s.replace('{}', '')
        # return s == ''
        
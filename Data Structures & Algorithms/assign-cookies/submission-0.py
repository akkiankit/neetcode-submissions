class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
    
        child_idx = 0
        cookie_idx = 0
    
        # One-pass algorithm with two pointers
        while child_idx < len(g) and cookie_idx < len(s):
            if s[cookie_idx] >= g[child_idx]:
                # This cookie can satisfy the current child
                child_idx += 1
            # Move to the next cookie regardless (greedy approach)
            cookie_idx += 1
    
        return child_idx
 
        
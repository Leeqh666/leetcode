class Solution:
    def maxDepth(self, s: str) -> int:
        my_max = 0
        n = 0

        for c in s:
            if c == '(':
                n += 1
                my_max = max(my_max, n)
            if c == ')':
                n -= 1
        
        return my_max


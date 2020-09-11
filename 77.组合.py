#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n is None or k is None:
            return []
        if n < k:
            return []
        if n == k:
            return [[i for i in range(1, n + 1)]]
        
        self.res = []
        self.backtrack(0,n,k,[])
        return self.res
        
    
    def backtrack(self, i, n, k, path):
        if k == 0:
            self.res.append(path.copy())
            return
        
        if k > (n - i):
            return
        
        for j in range(i + 1, n + 1):
            path.append(j)
            self.backtrack(j, n, k-1, path)
            path.pop()
        return

# @lc code=end

if __name__ == '__main__':
    obj = Solution()
    print(obj.combine(4, 2))
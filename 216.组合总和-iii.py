#
# @lc app=leetcode.cn id=216 lang=python3
#
# [216] 组合总和 III
#

# @lc code=start
from typing import List
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if n is None or k is None:
            return []

        if k == 0:
            return []
        if k >= n:
            return []

        candidates = [i for i in range(1, 10)]
        self.res = []
        self.path = []
        self.backtrack(candidates, k, n, self.path)
        return self.res

    def backtrack(self, candidates: List[int], k: List[int], n: int, path: List[int]):
        if k == 0 and n == 0:
            self.res.append(path.copy())
            return

        if n < 0 or k == 0:
            return
        
        for i,candidate in enumerate(candidates):
            path.append(candidate)
            self.backtrack(candidates[i + 1:], k - 1, n - candidate, path)
            path.pop()
        return

        


# @lc code=end


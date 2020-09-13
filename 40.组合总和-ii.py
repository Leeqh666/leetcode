#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#

# @lc code=start
from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        # res = []
        # def helper(tar, idx, cur):
        #     if tar == 0:
        #         res.append(cur[:])
        #         return
                
        #     for i in range(idx, len(candidates)):
        #         if candidates[i] > tar:
        #             break
        #         if i > idx and candidates[i] == candidates[i - 1]:
        #             continue
        #         cur.append(candidates[i])
        #         helper(tar - candidates[i], i + 1, cur)
        #         cur.pop()

        # candidates.sort()
        # helper(target, 0, [])
        # return res


        if candidates is None or target is None:
            return []
        
        candidates = sorted(candidates)

        self.res = []
        self.path = []

        self.backtrack(candidates, target, self.path)

        return self.res


        

    def backtrack(self, candidates: List[int], target: int, path) -> List[List[int]]:
        if target == 0:
            if not path in self.res:
                self.res.append(path.copy())
            return
        if target < 0:
            return
        
        for i, candidate in enumerate(candidates):
            path.append(candidate)
            self.backtrack(candidates[i + 1:], target - candidate, path)
            path.pop()
        return
# @lc code=end


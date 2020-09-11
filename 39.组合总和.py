#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
from typing import List
import bisect
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # dp = {i:[] for i in range(target+1)}

        # # 这里一定要将candidates降序排列
        # candidates = sorted(candidates, reverse=True)
        # for i in candidates:
        #     for j in range(i,target+1):
        #         if j==i:
        #             dp[j] = [[i]]
        #         else:
        #             dp[j].extend([x+[i] for x in dp[j-i]])
        # return dp[target]

        # if(not candidates):
        #     return []
        # n=len(candidates)
        # res=[]
        # candidates.sort()
        # def helper(i,tmp,target):
        #     if(target==0):
        #         res.append(tmp)
        #         return
        #     if(i==n or target<candidates[i]):
        #         return
        #     helper(i,tmp+[candidates[i]],target-candidates[i])
        #     helper(i+1,tmp,target)
        # helper(0,[],target)
        # return res
        
        if candidates is None or target is None:
            return []
        
        self.res = []

        candidates = sorted(candidates)
        path = []
        self.backtrack(candidates, target, path)
        return self.res

    
    def backtrack(self, candidates: List[int], target: int, path: List[int]) -> List[List[int]]:
        if target == 0:
            self.res.append(path.copy())
        
        if target < 0:
            return
        
        for i, candidate in enumerate(candidates):
            path.append(candidate)
            self.backtrack(candidates[i:], target - candidate, path)
            path.pop()
        
        return

            

# @lc code=end

if __name__ == '__main__':
    obj = Solution()
    print(obj.combinationSum([2,3,4,7], 7))
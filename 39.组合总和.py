#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = {i:[] for i in range(target+1)}

        # 这里一定要将candidates降序排列
        candidates = sorted(candidates, reverse=True)
        for i in candidates:
            for j in range(i,target+1):
                if j==i:
                    dp[j] = [[i]]
                else:
                    dp[j].extend([x+[i] for x in dp[j-i]])
        return dp[target]

# @lc code=end

if __name__ == '__main__':
    obj = Solution()
    obj.combinationSum([2,3,4,7], 7)
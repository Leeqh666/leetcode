#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#

# @lc code=start
from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if not nums:
            return False
        
        allSum = sum(nums)
        if allSum % 2 == 0:
            target = allSum / 2
        else:
            return False
        mem = {}

        def helper(nums, index, target):
            state = str(index) + '&' + str(target)
            if state in mem.keys():
                return mem[state]
            
            if index >= len(nums):
                return False
                
            if target == 0:
                return True
            elif target < 0:
                return False
            
            res = helper(nums, index + 1, target) or helper(nums, index + 1, target - nums[index])
            mem[state] = res
            return res
        
        return helper(nums, 0, target)
            
# @lc code=end


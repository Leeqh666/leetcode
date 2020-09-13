#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if nums is None or len(nums) == 0:
            return []
        
        for i, num in enumerate(nums):
            if target - num in nums:
                if i != nums.index(target - num):
                    return [i, nums.index(target - num)]
        
# @lc code=end


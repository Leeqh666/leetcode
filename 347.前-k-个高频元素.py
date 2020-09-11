#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#

# @lc code=start
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 0:
            return []

        count = {}
        for num in nums:
            if num in count.keys():
                count[num] += 1
            else:
                count[num] = 1
        
        result = sorted(count.items(), key=lambda x: x[1], reverse = True)

        return [result[i][0] for i in range(k)]


        
# @lc code=end


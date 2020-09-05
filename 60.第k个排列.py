#
# @lc app=leetcode.cn id=60 lang=python3
#
# [60] 第k个排列
#

# @lc code=start
from typing import List
import math
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        
        nums = [i for i in range(1, n + 1)]
        res = ''
        while len(nums) > 1:
            n = len(nums)
            tag = math.factorial(n - 1)
            target = int((k - 1) / tag)
            res += str(nums[target])
            nums.remove(nums[target])
            k = k - target * tag
            if k == 0:
                break
        strs = [str(i) for i in nums]
        res += ''.join(strs)

        return res

if __name__ == '__main__':
    obj = Solution()
    obj.getPermutation(3, 4)
# @lc code=end


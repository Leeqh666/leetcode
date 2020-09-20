from typing import List
from collections import defaultdict
class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        if not nums or not requests or len(nums) == 0 or len(requests) == 0:
            return 0
        
        mod = 1e9 + 7

        tag = defaultdict(int)

        for request in requests:
            for i in range(request[0], request[1] + 1):
                tag[i] += 1
        nums = sorted(nums, reverse=True)
        tag = sorted(tag.items(), key = lambda x:x[1], reverse=True)

        index = 0
        res = 0
        for item in tag:
            value = item[1]
            res += value * nums[index]
            res %= mod
            index += 1

        return res


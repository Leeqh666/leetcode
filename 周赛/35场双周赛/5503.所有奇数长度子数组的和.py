from typing import List
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        if not arr or len(arr) == 0:
            return 0
        res = sum(arr)

        n = len(arr)
        sub_len = 3
        while sub_len <= n:
            for i in range(0, n - sub_len + 1):
                res += sum(arr[i:i + sub_len])
            sub_len += 2
        
        return res

            


from typing import List

class Solution:
    def trimMean(self, arr: List[int]) -> float:
        if not arr:
            return 0
        
        n = len(arr)
        arr = sorted(arr)

        re_n = n * 0.05

        return sum(arr[re_n:n-re_n]) / (n * 0.9)
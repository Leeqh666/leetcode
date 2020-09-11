from typing import List
from math import sqrt
# class Solution:
#     def numTriplets_help(self, nums1: List[int], nums2: List[int]) -> int:
#         count = 0
#         nums1_2 = [num ** 2 for num in nums1]
        
#         nums2_mul = []

#         for i in range(len(nums2)):
#             for j in range(i + 1, len(nums2)):
#                 nums2_mul.append(nums2[i] * nums2[j])
        
#         for num1_2 in nums1_2:
#             count += nums2_mul.count(num1_2)

#         return count

#     def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
#         count = 0
#         count += self.numTriplets_help(nums1, nums2)
#         count += self.numTriplets_help(nums2, nums1)
#         return count    

class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        hashmap = {}
        m, n = len(nums1), len(nums2)
        for i in range(m):
            if nums1[i] not in hashmap:
                hashmap[nums1[i]] = 1
            else:
                hashmap[nums1[i]] += 1
        for j in range(n-1):
            for k in range(j+1,n):
                tmp = sqrt(nums2[j] * nums2[k])
                if tmp in hashmap:
                    res += hashmap[tmp]
        hashmap = {}
        for i in range(n):
            if nums2[i] not in hashmap:
                hashmap[nums2[i]] = 1
            else:
                hashmap[nums2[i]] += 1
        for j in range(m-1):
            for k in range(j+1,m):
                tmp = sqrt(nums1[j] * nums1[k])
                if tmp in hashmap:
                    res += hashmap[tmp]
        return res

if __name__ == "__main__":
    obj = Solution()
    obj.numTriplets([7, 4], [5, 2, 8, 9])
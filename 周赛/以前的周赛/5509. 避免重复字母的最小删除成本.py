from typing import List
# class Solution:
#     def minCost(self, s: str, cost: List[int]) -> int:
#         if len(s) == 1 or len(s) == 0:
#             return 0
#         res = 0

#         s = [str(c) for c in s]
#         i = 0
#         n = len(s)
#         while i < n - 1:
#             if s[i] == s[i + 1]:
#                 if cost[i] >= cost[i + 1]:
#                     res += cost[i + 1]
#                     del(s[i+1])
#                     del(cost[i+1])
#                 else:
#                     res += cost[i]
#                     del(s[i])
#                     del(cost[i])
#                 i -= 1
#                 n -= 1
#             i += 1
        
#         return res

class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        stack = []
        for i in range(len(s)):
            if not stack:
                stack.append((s[i],cost[i]))
            else:
                p,cost_p = stack[-1]
                if p != s[i]:
                    stack.append((s[i],cost[i]))
                else:
                    if cost_p < cost[i]:
                        stack.pop(-1)
                        stack.append((s[i],cost[i]))
        return sum(cost) - sum(i[1] for i in stack)

if __name__ == '__main__':
    obj = Solution()
    obj.minCost("bbbaaa", [4,9,3,8,8,9])

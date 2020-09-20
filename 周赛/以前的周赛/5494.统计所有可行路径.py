from typing import List
class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(locations)
        dp = [[0 for _ in range(fuel + 1)] for _ in range(n)]
        mod = 1e9 + 7
        dp[start][0] = 1
        for k in range(0, fuel + 1):
            for i in range(n):
                for j in range(n):
                    if j == i:
                        continue
                    if k + abs(locations[i] - locations[j]) > fuel:
                        continue
                    dp[j][k + abs(locations[i] - locations[j])] += dp[i][k]
                    dp[j][k + abs(locations[i] - locations[j])] %= mod

        res = 0
        for i in range(fuel + 1):
            res += dp[finish][i]
            res %= mod

        return res

if __name__ == '__main__':
    obj = Solution()
    print(obj.countRoutes([2,3,6,8,4],1,3,5))

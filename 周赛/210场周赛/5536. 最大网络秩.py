from collections import defaultdict
from typing import List
import itertools
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        if not roads or not n:
            return 0
        
        counts = defaultdict(int)
        for road in roads:
            counts[road[0]] += 1
            counts[road[1]] += 1

        counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        comb = []
        res = 0
        if counts[0][1] == counts[1][1]:
            for i,count in enumerate(counts):
                if count[1] == counts[0][1]:
                    comb.append(i)
                else:
                    break
            
            for i in itertools.combinations(comb, 2):
                temp_res = counts[i[0]][1] + counts[i[1]][1]
                if [counts[i[0]][0], counts[i[1]][0]] in roads or [counts[i[1]][0], counts[i[0]][0]] in roads:
                    temp_res -= 1
                
                res = max(res, temp_res)
            return res

        if counts[0][1] != counts[1][1]:
            for i, count in enumerate(counts):
                if i == 0:
                    continue
                if count[1] == counts[1][1]:
                    comb.append(i)
            
            for i in comb:
                temp_res = counts[0][1] + counts[i][1]
                if [counts[0][0], counts[i][0]] in roads or [counts[i][0], counts[0][0]] in roads:
                    temp_res -= 1

                res = max(res, temp_res)
            return res

if __name__ == '__main__':
    obj = Solution()
    obj.maximalNetworkRank(5,
[[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]])
            

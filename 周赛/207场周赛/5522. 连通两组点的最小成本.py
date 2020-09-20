from typing import List
from collections import defaultdict
class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        if not cost or len(cost) == 0:
            return 0
        res = 0
        size_1 = len(cost)
        size_2 = len(cost[0])
        if size_1 == 1:
            return cost[0][0]
        if size_2 == 1:
            for i in range(size_1):
                res += cost[i][0]
            return res
        combine = {}
        re_combine = defaultdict(list)
        tag = [False] * size_2
        for i in range(size_1):
            temp = min(cost[i])
            index = cost[i].index(temp)
            res += temp
            combine[i] = index
            re_combine[index].append(i)
            tag[index] = True

        for j in range(size_2):
            cost_j = [0] * size_1
            if tag[j]:
                continue
            else:
                for i in range(size_1):
                    if len(re_combine[combine[i]]) > 1:
                        cost_j[i] = cost[i][j] - cost[i][combine[i]]
                    else:
                        cost_j[i] = cost[i][j]
                min_cost_j = min(cost_j)
                temp_index = cost_j.index(min_cost_j)
                re_combine[combine[temp_index]].remove(temp_index)
                combine[temp_index] = j
                res += min_cost_j
        
        return res




            
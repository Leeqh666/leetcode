import collections
from typing import List
class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        res = [0] * (n-1)
        dic = collections.defaultdict(list)
        for x, y in edges:
            dic[x].append(y)
            dic[y].append(x)
        dis = collections.defaultdict(int)
        
        # 记录节点间的路径长度,将每个节点都作为根节点进行一次深度优先遍历
        for x in range(1, n+1):
            visited = set()
            queue = [x]
            path = 0
            while queue:
                path += 1
                for i in range(len(queue)):
                    cur = queue.pop(0)
                    visited.add(cur)
                    for j in dic[cur]:
                        if j not in visited:
                            queue.append(j)
                            dis[(x, j)] = path
        # tmp数组记录状态压缩后每一种子节点集合的情况 ，此处利用位运算进行状态压缩   
        for i in range(1, 2**n):
            tmp = []
            cur = 0
            # 每个位置如果是1的话就压入，否则跳过
            while i:
                cur += 1
                if i % 2 == 1:
                    tmp.append(cur)
                i >>= 1
            if len(tmp) <= 1:
                continue
            road = 0
            ## 记录状态压缩后不完全图的边的数量
            for x, y in edges:
                if x in tmp and y in tmp:
                    road += 1
            ## 边数不等于节点数-1不满足树的定义
            if road < len(tmp) - 1:
                continue
            maxd = 0
            ## 记录最大路径更新结果
            for i in range(len(tmp)):
                for j in range(i + 1, len(tmp)):
                    maxd = max(dis[tmp[i], tmp[j]], maxd)
            res[maxd-1] += 1
        return res
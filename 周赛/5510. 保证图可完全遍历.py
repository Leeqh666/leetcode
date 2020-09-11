from typing import List
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        # ufs1: Alice(type1+3), ufs2: Bob(type2+3), ufs3: type3 
        ufs1, ufs2, ufs3 = UFSet(n), UFSet(n), UFSet(n)
        edgeNum = len(edges)
        for i in range(edgeNum):
            if edges[i][0] != 2:
                ufs1.union(edges[i][1] - 1, edges[i][2] - 1)
            if edges[i][0] != 1:
                ufs2.union(edges[i][1] - 1, edges[i][2] - 1)
            if edges[i][0] == 3:
                ufs3.union(edges[i][1] - 1, edges[i][2] - 1)
        if ufs1.count() > 1 or ufs2.count() > 1:
            return -1

        minEdgeNum = (ufs3.count() - 1) * 2    # edges between closures. Connected by type1 and type2 edge.
        for i in range(n):
            if ufs3.arr[i] < -1:
                minEdgeNum += (0 - ufs3.arr[i] - 1)   # edges in closures. Connected by type3 edge.
        return edgeNum - minEdgeNum

class UFSet():
    def __init__(self, n):
        self.arr = [-1] * n
    def find(self, x):
        while self.arr[x] >= 0:
            x = self.arr[x]
        return x
    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return
        if self.arr[rx] < self.arr[ry]:
            rx, ry = ry, rx
        self.arr[ry] += self.arr[rx]
        self.arr[rx] = ry
    def count(self):
        res = 0
        for a in self.arr:
            if a < 0:
                res += 1
        return res


"""
from typing import List
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        if n == 1:
            return len(edges)
        count = 0
        A_map = [-1] * (n + 1)
        B_map = [-1] * (n + 1)
        def find(map, x):
            while map[x] >= 0:
                if map[x] == x:
                    break
                x = map[x]
            return x

        A_map[0] = B_map[0] = 0
        
        A_edges = []
        B_edges = []
        for edge in edges:
            if edge[0] == 1:
                A_edges.append(edge)
            elif edge[0] == 2:
                B_edges.append(edge)
            else:
                if find(A_map, edge[1]) == find(A_map, edge[2]):
                    count += 1
                else:
                    A_map[edge[1]] = A_map[edge[2]] = min(find(A_map, edge[1]), find(A_map, edge[2]))
                    B_map[edge[1]] = B_map[edge[2]] = min(find(A_map, edge[1]), find(A_map, edge[2]))

                
        
        for edge in A_edges:
            if find(A_map, edge[1]) == find(A_map, edge[2]):
                count += 1
            else:
                A_map[edge[1]] = A_map[edge[2]] = min(find(A_map, edge[1]), find(A_map, edge[2]))

        for edge in B_edges:
            if find(B_map, edge[1]) == find(B_map, edge[2]):
                count += 1
            else:
                B_map[edge[1]] = B_map[edge[2]] = min(find(A_map, edge[1]), find(A_map, edge[2]))
        
        if -1 in A_map or -1 in B_map:
            return -1
        
        return count

if __name__ == "__main__":
    obj = Solution()
    obj.maxNumEdgesToRemove(4,
[[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]])
"""
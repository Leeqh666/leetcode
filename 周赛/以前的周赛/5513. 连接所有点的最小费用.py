from typing import List
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if points is None:
            return 0
        n = len(points)
        self.res = 0
        def help(x, y):
            return abs(x[0] - y[0]) + abs(x[1] - y[1])
        if n == 0 or n == 1:
            return 0
        points_index = set(range(n))
        dis = [float('inf') for _ in range(n)]
        current = points_index.pop()
        while len(points_index) > 0:
            for other in points_index:
                temp = help(points[current], points[other])
                if temp < dis[other]:
                    dis[other] = temp
            temp_res = min(dis)
            self.res += temp_res
            current = dis.index(temp_res)
            dis[current] = float('inf')
            points_index.remove(current)
        
        return self.res
            

if __name__ == '__main__':
    obj = Solution()
    obj.minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]])

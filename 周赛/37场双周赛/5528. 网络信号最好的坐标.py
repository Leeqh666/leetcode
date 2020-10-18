from typing import List
from collections import defaultdict
from math import floor, sqrt

class Solution:
    def bestCoordinate(self, t: List[List[int]], r: int) -> List[int]:
        ans=defaultdict(int)
        for x,y,q in t:
            for i in range(-r,r+1):
                for j in range(-r,r+1):
                    nx,ny=x+i,y+j
                    d=(nx-x)**2+(ny-y)**2
                    if d<=r**2:
                        ans[(nx,ny)]+=int(floor(q/(1+sqrt(d))))
        return sorted([(i,j) for i,j in ans.items()],key=lambda x:(-x[1],x[0]))[0][0]

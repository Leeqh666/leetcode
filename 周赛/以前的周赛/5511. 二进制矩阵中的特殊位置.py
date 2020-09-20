from typing import List
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        if mat is None or len(mat) == 0:
            return 0
        n = len(mat)
        self.res = 0
        for ma in mat:
            if sum(ma) != 1:
                continue
            else:
                for i,m in enumerate(ma):
                    if m == 1:
                        target = 0
                        for j in range(n):
                            target += mat[j][i]
                        if target == 1:
                            self.res += 1
        return self.res


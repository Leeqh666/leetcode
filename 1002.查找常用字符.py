#
# @lc app=leetcode.cn id=1002 lang=python3
#
# [1002] 查找常用字符
#

# @lc code=start
from collections import Counter
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        # if not A:
        #     return []
        # if len(A) == 1:
        #     return list(A[0])
        # res = [float('inf')] * 26
        # for a in A:
        #     for tag in range(97, 97 + 26):
        #         res[tag - 97] = min(res[tag - 97], a.count(chr(tag)))
        # ret = []
        # for i in range(26):
        #     ret.extend([chr(97 + i)] * res[i])
        # return ret
    

        res = None
        for a in A:
            c = Counter(a)
            if res is None:
                res = c
            else:
                res &= c
        return list(res.elements())
# @lc code=end


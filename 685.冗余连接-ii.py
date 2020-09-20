#
# @lc app=leetcode.cn id=685 lang=python3
#
# [685] 冗余连接 II
#

# @lc code=start
from typing import List
from collections import defaultdict
class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        if not edges:
            return []
        map = defaultdict(list)
        for edg in edges:
            node_in = edg[0]
            node_out = edg[1]

            if node_out in map[node_in]:
                return edg
            else:
                map[node_in].append(node_out)

            for key in map.keys():
                if node_in in map[key]:
                    if node_out == key or node_out in map[key]:
                        return edg
                    else:
                        map[key].append(node_out)
                else:
                    continue
        
        return []

            
        
# @lc code=end


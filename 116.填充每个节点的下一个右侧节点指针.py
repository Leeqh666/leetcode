#
# @lc app=leetcode.cn id=116 lang=python3
#
# [116] 填充每个节点的下一个右侧节点指针
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        queue = []
        queue.append(root)
        queue.append(None)
        while queue:
            temp_queue = []
            while queue:
                cur = queue.pop(0)
                if cur.left:
                    temp_queue.append(cur.left)
                if cur.right:
                    temp_queue.append(cur.right)
                if queue:
                    cur.next = queue[0]
            queue = temp_queue
        return root
# @lc code=end


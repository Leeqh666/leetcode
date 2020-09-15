#
# @lc app=leetcode.cn id=637 lang=python3
#
# [637] 二叉树的层平均值
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from typing import List
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if root is None:
            return []
        self.res = []
        queue = []
        queue.append((root, 0))

        current_depth = 0
        temp = []
        while len(queue) != 0:
            node, depth = queue.pop(0)
            if depth != current_depth:
                self.res.append(sum(temp)/len(temp))
                temp = []
                temp.append(node.val)
                current_depth += 1
            else:
                temp.append(node.val)
            
            if node.left is not None:
                queue.append((node.left, depth + 1))
            if node.right is not None:
                queue.append((node.right, depth + 1))

        self.res.append(sum(temp)/len(temp))
        return self.res

# @lc code=end


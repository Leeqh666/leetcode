#
# @lc app=leetcode.cn id=968 lang=python3
#
# [968] 监控二叉树
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        self.NO_CAMERA = 0
        self.HAS_CAMERA = 1
        self.NO_NEEDED = 2

        self.res = 0

        if not root:
            return 0

        if self.dfs(root) == self.NO_CAMERA:
            self.res += 1

        return self.res

    def dfs(self, root: TreeNode) -> int:
        if not root:
            return self.NO_NEEDED
        
        left = self.dfs(root.left)
        right = self.dfs(root.right)

        if left == self.NO_CAMERA or right == self.NO_CAMERA:
            self.res += 1
            return self.HAS_CAMERA
        
        return self.NO_NEEDED if left == self.HAS_CAMERA or right == self.HAS_CAMERA else self.NO_CAMERA 

# @lc code=end


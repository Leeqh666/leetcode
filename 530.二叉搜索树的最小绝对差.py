#
# @lc app=leetcode.cn id=530 lang=python3
#
# [530] 二叉搜索树的最小绝对差
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        if not root:
            return 0

        nums = []

        def dfs(node, nums):
            if not node:
                return
            dfs(node.left, nums)
            nums.append(node.val)
            dfs(node.right, nums)
        
        res = float('inf')
        for i in range(len(nums) - 1):
            res = min(nums[i + 1] - nums[i], res)
        
        return res


# @lc code=end


#
# @lc app=leetcode.cn id=617 lang=python3
#
# [617] 合并二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 and not t2:
            return None
        
        def merge(t1, t2):
            if not t1 and not t2:
                return None
            elif not t1 and t2:
                return t2
            elif t1 and not t2:
                return t1
            
            val = t1.val + t2.val
            current = TreeNode(val)
            current.left = merge(t1.left, t2.left)
            current.right = merge(t1.right, t2.right)

            return current
        
        return merge(t1, t2)
        
# @lc code=end


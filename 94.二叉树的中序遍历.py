#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # if root is None:
        #     return []
        
        # res = []
        # def help(root):
        #     if root.left:
        #         help(root.left)
        #     res.append(root.val)
        #     if root.right:
        #         help(root.right)
        #     return
        
        # help(root)

        # return res
        if root is None:
            return []
        res = []
        stack = []
        stack.append((root, 0))
        while len(stack) != 0:
            current, tag = stack.pop()
            if tag == 0:
                stack.append((current, 1))                
                if current.left:
                    stack.append((current.left, 0))
            if tag == 1:
                res.append(current.val)
                if current.right:
                    stack.append((current.right, 0))
        return res

if __name__ == '__main__':
    obj = Solution()
    root = TreeNode(1)
    root.left = None
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    root.right.right = None
    obj.inorderTraversal(root)

# @lc code=end


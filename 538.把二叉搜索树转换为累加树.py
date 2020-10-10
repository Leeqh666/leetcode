#
# @lc app=leetcode.cn id=538 lang=python3
#
# [538] 把二叉搜索树转换为累加树
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        
        stack = []
        cache = 0

        stack.append((root, 0))

        while len(stack) != 0:
            current, tag = stack.pop(-1)
            if tag == 0:
                stack.append((current, 1))
                if current.right:
                    stack.append((current.right, 0))
                continue

            if tag == 1:
                current.val += cache
                cache = current.val

                if current.left:
                    stack.append((current.left, 0))
        
        return root
# class Solution:
#     def convertBST(self, root: TreeNode) -> TreeNode:
#         self.sum = 0
#         def dfs(node):
#             if not node: return
#             dfs(node.right)
#             self.sum += node.val
#             node.val = self.sum
#             dfs(node.left)
#         dfs(root)
#         return root            


# @lc code=end


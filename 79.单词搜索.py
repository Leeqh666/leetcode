#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#

# @lc code=start
from typing import List
import copy
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if board is None or len(board) == 0:
            return False
        
        m = len(board)
        n = len(board[0])
        mask = [[True for _ in range(n)] for _ in range(m)]

        def dfs(i, j, target, words, mask):
            if target == len(words):
                return True
            else:
                if  i - 1 >= 0 and board[i - 1][j] == words[target] and mask[i - 1][j]:
                    temp = copy.deepcopy(mask)
                    temp[i - 1][j] = False
                    if dfs(i - 1, j, target + 1, words, temp):
                        return True
                if i + 1 < m and board[i + 1][j] == words[target] and mask[i + 1][j]:
                    temp = copy.deepcopy(mask)
                    temp[i + 1][j] = False
                    if dfs(i + 1, j, target + 1, words, temp):
                        return True
                if j - 1 >= 0 and board[i][j - 1] == words[target] and mask[i][j - 1]:
                    temp = copy.deepcopy(mask)
                    temp[i][j - 1] = False
                    if dfs(i, j - 1, target + 1, words, temp):
                        return True
                if j + 1 < n and board[i][j + 1] == words[target] and mask[i][j + 1]:
                    temp = copy.deepcopy(mask)
                    temp[i][j + 1] = False
                    if dfs(i, j + 1, target + 1, words, temp):
                        return True
                
            return False  

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    mask[i][j] = False
                    if dfs(i,j,1,word, mask):
                        return True
                    mask[i][j] = True
        
        return False


# @lc code=end


#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s is None or len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        
        max = 0
        sub_string = [s[0]]
        for i in range(1, len(s)):
            if s[i] in sub_string:
                n = len(sub_string)
                max = n if n >= max else max
                index = sub_string.index(s[i])
                start = index + 1
                sub_string = sub_string[start:]
            
            sub_string.append(s[i])
        n = len(sub_string)
        max = n if n >= max else max
        return max

# @lc code=end


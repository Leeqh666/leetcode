class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        if not s:
            return -1
        
        query = {}
        target_c = ''
        max_len = 0
        for i,c in enumerate(s):
            if c not in query.keys():
                query[c] = i
            else:
                temp = i - query[c]
                if temp > max_len:
                    max_len = temp
                    target_c = c
        if target_c == '':
            return -1
        return max_len - 1



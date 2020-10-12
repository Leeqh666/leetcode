class Solution:
    # 中心分割
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        le = len(a)
        l = le // 2 - 1
        r = le // 2  if le % 2 == 0 else le // 2 + 1

        a_flag = True
        b_flag = True
        while l > -1 and r < le:
            if a_flag and a[l] != a[r]:
                a_flag = False
            if b_flag and b[l] != b[r]:
                b_flag = False
            
            if a_flag or b_flag:
                l -= 1
                r += 1
            else:
                break

        if a[:l + 1] == b[r:][::-1] or b[:l + 1] == a[r:][::-1]:
            return True

        return False
    
    # 去掉相应的头和尾后，判断中间剩余部分是否回文
    # def checkPalindromeFormation(self, a: str, b: str) -> bool:
    #     # 判断a, b是否回文串
    #     def is_palindrome(s):
    #         return s == s[::-1]

    #     # a,b任意一个为回文串的情况，则返回true
    #     has_palindrome = is_palindrome(a) or is_palindrome(b)
    #     if has_palindrome:
    #         return True
    #     # a,b都不是回文串的情况
    #     # a头b尾：判断a[i]==b[len-i-1]是否成立，直到不满足时，判断，可回文的字符和是否等于字符串长，不等于则判断，a/b中i:len-i-1子串是否回文，如果回文，则可回文
    #     # b头a尾，同上
    #     str_len = len(a)
    #     for i in range(str_len):
    #         if a[i] != b[str_len - i - 1]:
    #             if i ==0:
    #                 break
    #             if is_palindrome(a[i:str_len - i]) or is_palindrome(b[i:str_len - i]):
    #                 return True
    #     for i in range(str_len):
    #         if b[i] != a[str_len - i - 1]:
    #             if i ==0:
    #                 break
    #             if is_palindrome(a[i:str_len - i]) or is_palindrome(b[i:str_len - i]):
    #                 return True
    #     return False
if __name__ == '__main__':
    obj = Solution()
    print(obj.checkPalindromeFormation('abda', 'acmc'))

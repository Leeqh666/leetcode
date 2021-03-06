#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 递归方法
        # if not head or not head.next:
        #     return head
        
        # tail = self.reverseList(head.next)
        # head.next.next = head
        # head.next = None
        # return tail

        # 迭代方法
        # if not head:
        #     return None

        pre = None
        cur = head    
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        
        return pre
            

# @lc code=end


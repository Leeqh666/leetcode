#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return None
        if not l1:
            return l2
        if not l2:
            return l1
        l1_list = []
        l2_list = []
        while l1:
            l1_list.append(str(l1.val))
            l1 = l1.next
        while l2:
            l2_list.append(str(l2.val))
            l2 = l2.next
        l1_str = ''.join(l1_list[::-1])
        l2_str = ''.join(l2_list[::-1])
        res = int(l1_str) + int(l2_str)
        head = ListNode(0)
        temp = head
        for c in str(res)[:0:-1]:
            temp.val = int(c)
            temp.next = ListNode(0)
            temp = temp.next
        temp.val = int(str(res)[0])
        return head
        
        
        
# @lc code=end
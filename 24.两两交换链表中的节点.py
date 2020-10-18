#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # 迭代写法
        # dummy = ListNode(0, head)

        # prev = dummy
        # while head and head.next:
        #     prev.next = head.next
        #     head.next = head.next.next
        #     prev.next.next = head

        #     prev = head
        #     head = head.next
        # return dummy.next
    
        # 递归写法
        if not head or not head.next:
            return head
        the_next = head.next
        head.next = self.swapPairs(the_next.next)
        the_next.next = head
        return the_next
    


# @lc code=end


#
# @lc app=leetcode.cn id=206 lang=python
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 参考
# https: // blog.csdn.net/gongliming_/article/details/88712221

# https: // leetcode-cn.com/problems/reverse-linked-list/solution/fan-zhuan-lian-biao-by-leetcode-solution-d1k2/
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 1. 迭代 将指针顺序弄反
        # pre = None
        # tail = head
        # while tail:
        #     tail = head.next
        #     # print(head.val)
        #     head.next = pre
        #     pre = head
        #     head = tail
        # return pre

        # 2. 递归 难写
        if head == None or head.next == None:
            return head
        newHead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return newHead

# @lc code=end

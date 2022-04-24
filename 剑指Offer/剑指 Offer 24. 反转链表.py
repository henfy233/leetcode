# -*- encoding: utf-8 -*-
'''
@File    :   剑指 Offer 24. 反转链表.py
@Time    :   2022/04/21 16:08:40
@Author  :   henfy
@Diffi   :   Easy
@Version :   1.0

题目：https://leetcode-cn.com/problems/fan-zhuan-lian-biao-lcof/
'''

# Definition for singly-linked list.
# 不太会


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 迭代
        # https://leetcode-cn.com/problems/fan-zhuan-lian-biao-lcof/solution/jian-zhi-offer-24-fan-zhuan-lian-biao-die-dai-di-2/
        # pre = None
        # tail = head
        # while tail:
        #     tail = head.next
        #     head.next = pre
        #     pre = head
        #     head = tail
        # return pre

        # 递归
        def recur(cur, pre):
            if not cur:
                return pre
            res = recur(cur.next, cur)
            cur.next = pre
            return res
        return recur(head, None)

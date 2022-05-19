# -*- encoding: utf-8 -*-
'''
@File    :   剑指 Offer 18. 删除链表的节点.py
@Time    :   2022/05/13 21:41:27
@Author  :   henfy
@Diffi   :   Easy

题目：https://leetcode.cn/problems/shan-chu-lian-biao-de-jie-dian-lcof/
'''

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        # 双指针
        if head.val == val:
            return head.next
        pre, cur = head, head.next
        while cur and cur.val != val:
            pre, cur = cur, cur.next
        if cur:
            pre.next = cur.next
        return head

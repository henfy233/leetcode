# -*- encoding: utf-8 -*-
'''
@File    :   剑指 Offer 25. 合并两个排序的链表.py
@Time    :   2022/05/14 23:44:17
@Author  :   henfy
@Diffi   :   Easy
@Method  :   双指针

题目：https://leetcode.cn/problems/he-bing-liang-ge-pai-xu-de-lian-biao-lcof/
'''

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 双指针
        head = tmp = ListNode(0)
        while l1 and l2:
            if l1.val >= l2.val:
                tmp.next = l2
                l2 = l2.next
            else:
                tmp.next = l1
                l1 = l1.next
            tmp = tmp.next
        tmp.next = l1 if l1 else l2
        return head

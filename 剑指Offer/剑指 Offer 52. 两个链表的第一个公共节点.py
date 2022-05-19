# -*- encoding: utf-8 -*-
'''
@File    :   剑指Offer52.两个链表的第一个公共节点.py
@Time    :   2021/07/21 10:06:25
@Author  :   henfy
@Diffi   :   Easy
@Method  :   双指针

题目：https://leetcode-cn.com/problems/liang-ge-lian-biao-de-di-yi-ge-gong-gong-jie-dian-lcof/
'''

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # 双指针
        A, B = headA, headB
        while A != B:
            A = A.next if A else headB
            B = B.next if B else headA
        return A

        # 哈希集合
        # d = {}
        # while headA:
        #     d[headA] = headA
        #     headA = headA.next
        # while headB:
        #     if d.get(headB):
        #         return headB
        #     headB = headB.next
        # return None

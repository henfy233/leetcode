# -*- encoding: utf-8 -*-
'''
@File    :   剑指Offer52.两个链表的第一个公共节点.py
@Time    :   2021/07/21 10:06:25
@Author  :   henfy
@Diffi   :   Easy
@Version :   1.0

题目：https://leetcode-cn.com/problems/liang-ge-lian-biao-de-di-yi-ge-gong-gong-jie-dian-lcof/
'''
# python 题解
# https://qingfengpython.cn/#/markdown/Algorithm/%E9%93%BE%E8%A1%A8/%E5%89%91%E6%8C%87Offer52.%E4%B8%A4%E4%B8%AA%E9%93%BE%E8%A1%A8%E7%9A%84%E7%AC%AC%E4%B8%80%E4%B8%AA%E5%85%AC%E5%85%B1%E8%8A%82%E7%82%B9

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
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

        # 双指针
        nodeA, nodeB = headA, headB
        while nodeA != nodeB:
            nodeA = nodeA.next if nodeA else headB
            nodeB = nodeB.next if nodeB else headA
        return nodeA

# -*- encoding: utf-8 -*-
'''
@File    :   剑指 Offer 22. 链表中倒数第k个节点.py
@Time    :   2021/09/02 00:20:09
@Author  :   henfy
@Diffi   :   Easy
@Method  :   双指针

题目：https://leetcode-cn.com/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof/
'''

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        pre, cur = head, head
        for i in range(k):
            cur = cur.next
        print('cur', cur.val)
        while cur:
            pre = pre.next
            cur = cur.next
        return pre

        # 1. 顺序查找
        # https://leetcode-cn.com/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof/solution/lian-biao-zhong-dao-shu-di-kge-jie-dian-1pz9l/
        # node, n = head, 0
        # while node:
        #     node = node.next
        #     n += 1
        # node = head
        # for _ in range(n-k):
        #     node = node.next
        # return node

        # 2. 双指针
        # fast, slow = head, head
        # while fast and k > 0:
        #     fast, k = fast.next, k - 1
        # while fast:
        #     fast, slow = fast.next, slow.next
        # return slow

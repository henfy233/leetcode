# -*- encoding: utf-8 -*-
'''
@File    :   剑指 Offer 06. 从尾到头打印链表.py
@Time    :   2022/04/21 15:55:55
@Author  :   henfy
@Diffi   :   Easy
@Version :   1.0

题目：https://leetcode-cn.com/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof/
'''

# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        # arr, ans = [], []
        # while head:
        #     arr.append(head.val)
        #     head = head.next
        # # print('arr',arr)
        # for _ in range(len(arr)):
        #     ans.append(arr.pop())
        # return ans

        # 递归法
        return self.reversePrint(head.next) + [head.val] if head else []

        # 辅助栈法
        # stack = []
        # while head:
        #     stack.append(head.val)
        #     head = head.next
        # return stack[::-1]

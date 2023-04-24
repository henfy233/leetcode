# -*- encoding: utf-8 -*-
'''
@File    :   141. 环形链表.py
@Time    :   2023/04/24 22:06:18
@Author  :   henfy
@Diffi   :   Easy
@Method  :   哈希表、链表、双指针
@Question:   https://leetcode.cn/problems/linked-list-cycle/
@Answer  :
'''

# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

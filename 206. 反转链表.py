# -*- encoding: utf-8 -*-
'''
@File    :   206. 反转链表.py
@Time    :   2021/08/03 18:49:48
@Author  :   henfy
@Diffi   :   Easy
@Method  :   迭代、递归
@Question:   https://leetcode-cn.com/problems/reverse-linked-list/
@Answer  :   https://leetcode.cn/problems/reverse-linked-list/solutions/36710/dong-hua-yan-shi-206-fan-zhuan-lian-biao-by-user74/
'''

# NOTE 做过
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head: ListNode) -> ListNode:
        # 1. 迭代 将指针顺序弄反
        pre = None
        tail = head
        while tail:
            tail = head.next
            head.next = pre
            pre = head
            head = tail
        return pre

        # 2. 递归 难写
        # if head == None or head.next == None:
        #     return head
        # newHead = self.reverseList(head.next)
        # head.next.next = head
        # head.next = None
        # return newHead

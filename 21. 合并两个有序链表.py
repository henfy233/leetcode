# -*- encoding: utf-8 -*-
'''
@File    :   21. 合并两个有序链表.py
@Time    :   2021/08/03 20:19:08
@Author  :   henfy
@Diffi   :   Easy
@Version :   1.0

题目：https://leetcode-cn.com/problems/merge-two-sorted-lists/submissions/
'''


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 自己做 链表连接处不会相连 有疑惑
        # l = head = ListNode()
        # while l1 or l2:
        #     if not l1:
        #         l.next = l2
        #         l2 = l2.next
        #         l = l.next
        #         continue
        #     elif not l2:
        #         l.next = l1
        #         l = l.next
        #         l1 = l1.next
        #         continue
        #     if l1.val <= l2.val:
        #         l.next = l1
        #         l = l.next
        #         l1 = l1.next
        #     else:
        #         l.next = l2
        #         l = l.next
        #         l2 = l2.next
        # return head.next

        # 1. 与自己做法相同，更加简洁
        # 递归法
        dummy = ListNode(0)  # 哑节点
        move = dummy
        # 开始比较
        while l1 and l2:
            if l1.val <= l2.val:
                move.next = l1
                l1 = l1.next
            else:
                move.next = l2
                l2 = l2.next
            # 每次比较完 要移动一位
            move = move.next
        move.next = l1 if l1 else l2  # 追加不为空的 链表
        return dummy.next  # 返回 表头哑节点，下一条
        # 执行用时：24 ms, 在所有 Python 提交中击败了69.82 % 的用户
        # 内存消耗：13 MB, 在所有 Python 提交中击败了71.42 % 的用户

        # 递归解法
        # 判断跳出递归条件
        # if l1 is None:
        #     return l2
        # if l2 is None:
        #     return l1
        # # 单次递归方法，比较当前节点值
        # if l1.val <= l2.val:
        #     l1.next = self.mergeTwoLists(l1.next, l2)
        #     return l1
        # else:
        #     l2.next = self.mergeTwoLists(l1, l2.next)
        #     return l2
        # 执行用时：24 ms, 在所有 Python 提交中击败了69.82 % 的用户
        # 内存消耗：12.9 MB, 在所有 Python 提交中击败了87.30 % 的用户

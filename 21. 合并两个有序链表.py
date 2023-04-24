# -*- encoding: utf-8 -*-
'''
@File    :   21. 合并两个有序链表.py
@Time    :   2021/08/03 20:19:08
@Author  :   henfy
@Diffi   :   Easy
@Method  :   迭代、递归
@Question:   https://leetcode-cn.com/problems/merge-two-sorted-lists/submissions/
@Answer  :   https://leetcode.cn/problems/merge-two-sorted-lists/solutions/226408/he-bing-liang-ge-you-xu-lian-biao-by-leetcode-solu/
'''


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
      # NOTE 做过
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

        # 1. 迭代，更加简洁
        dummy = ListNode(0)  # 伪节点
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

        # 2.递归
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

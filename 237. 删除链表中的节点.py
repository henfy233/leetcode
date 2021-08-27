# -*- encoding: utf-8 -*-
'''
@File    :   237. 删除链表中的节点.py
@Time    :   2021/07/31 20:44:29
@Author  :   henfy
@Diffi   :   Easy
@Version :   1.0

题目：https://leetcode-cn.com/problems/delete-node-in-a-linked-list/
'''


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# 这题直接给出要删除链表的结点，而不是给你头结点，这不能在 vscode运行
class Solution(object):
    def insert(self, res):
        node = ListNode(res[0])
        tmp = node
        for i in res[1:]:
            head = ListNode(i)
            tmp.next = head
            tmp = tmp.next
        return node

    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # while node:
        #     print(node.val)
        #     node = node.next
        # print('l',l)
        node.val = node.next.val
        node.next = node.next.next
        return node

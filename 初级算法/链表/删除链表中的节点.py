#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   删除链表中的节点.py
@Time    :   2021/07/31 20:44:29
@Author  :   henfy
@Version :   1.0
'''

# here put the import lib

# Definition for singly-linked list.


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


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([4, 5, 1, 9], 5, [4, 1, 9]),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        l = s.insert(*test)
        test_result = s.deleteNode(l)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)

#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   反转链表.py
@Time    :   2021/08/03 18:49:48
@Author  :   henfy
@Version :   1.0
'''

# here put the import lib


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# 与206题相同
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 自己想，用时慢，内存小
        # res = []
        # tmp = head
        # while tmp:
        #     # print(tmp.val)
        #     res.append(tmp.val)
        #     tmp = tmp.next
        # # print(res)
        # right = len(res)-1
        # tmp = head
        # while tmp:
        #     tmp.val = res[right]
        #     tmp = tmp.next
        #     right -= 1
        # return head

        # 1. 迭代 将指针顺序弄反
        # pre = None
        # tail = head
        # while tail:
        #     tail = head.next
        #     head.next = pre
        #     pre = head
        #     head = tail
        # return pre
        # 执行用时：16 ms, 在所有 Python 提交中击败了94.08 % 的用户
        # 内存消耗：14.8 MB, 在所有 Python 提交中击败了85.44 % 的用户

        # 2. 递归 难写
        if head == None or head.next == None:
            return head
        newHead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return newHead
        # 执行用时：84 ms, 在所有 Python 提交中击败了5.06%的用户
        # 内存消耗：18.3 MB, 在所有 Python 提交中击败了6.77%的用户


if __name__ == '__main__':
    s = Solution()
    test_list = [
        (),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.reverseList(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)

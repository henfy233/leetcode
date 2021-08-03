#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   合并两个有序链表.py
@Time    :   2021/08/03 20:19:08
@Author  :   henfy
@Version :   1.0
'''

# here put the import lib

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """


if __name__ == '__main__':
   s = Solution()
   test_list = [
       (),
   ]

   for test_index, test_case in enumerate(test_list, start=1):
       *test, result = test_case
       test_result = s.mergeTwoLists(*test)
       if test_result != result:
           raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (test_index, result, test_result))
       print("test_case %d succeed." % test_index)

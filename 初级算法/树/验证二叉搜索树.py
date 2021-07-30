#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   验证二叉搜索树.py
@Time    :   2021/07/29 23:39:01
@Author  :   henfy
@Version :   1.0
'''

# here put the import lib

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """


if __name__ == '__main__':
   s = Solution()
   test_list = [
       (),
   ]

   for test_index, test_case in enumerate(test_list, start=1):
       *test, result = test_case
       test_result = s.isValidBST(*test)
       if test_result != result:
           raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (test_index, result, test_result))
       print("test_case %d succeed." % test_index)

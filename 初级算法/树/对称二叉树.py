#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   对称二叉树.py
@Time    :   2021/07/30 13:21:03
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


# 难题，还需重复做
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # 1. 递归  自己没有想法
        if not root:
            return True

        def dfs(left, right):
            # 左右都为空返回True
            if not left and not right:
                return True
            # 只有一个为空返回False,值不一样返回False
            if not left or not right or left.val != right.val:
                return False
            return dfs(left.left, right.right) and dfs(right.left, left.right)
        return dfs(root.left, root.right)
        # 执行用时：20 ms, 在所有 Python 提交中击败了80.67 % 的用户
        # 内存消耗：12.9 MB, 在所有 Python 提交中击败了99.94 % 的用户

        # 迭代一,这个很复杂，不推荐
        # if not root:
        #     return True
        # new_list = [root.left, root.right]
        # while new_list:
        #     lens = len(new_list)
        #     new = new_list
        #     new_list = []
        #     value_list = []
        #     if new.count(None) == lens:
        #         return True
        #     for n in new:
        #         if n:
        #             value_list.append(n.val)
        #             new_list.extend([n.left, n.right])
        #         else:
        #             value_list.append(None)
        #             new_list.extend([None, None])
        #     if value_list != value_list[::-1]:
        #         return False
        # return True

        # 迭代二 这个可以，原题用队列处理，这里用数组
        # if not root:
        #     return True
        # new_list = [root.left, root.right]
        # while new_list:
        #     left, right = new_list[:2]
        #     new_list = new_list[2:]
        #     if not left and not right:
        #         continue
        #     if not left or not right or left.val != right.val:
        #         return False
        #     new_list.extend([left.left, right.right])
        #     new_list.extend([left.right, right.left])
        # return True
        # 执行用时：24 ms, 在所有 Python 提交中击败了60.00 % 的用户
        # 内存消耗：13.2 MB, 在所有 Python 提交中击败了61.17 % 的用户


if __name__ == '__main__':
    s = Solution()
    test_list = [
        (),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.isSymmetric(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)

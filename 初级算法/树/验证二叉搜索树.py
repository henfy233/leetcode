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
        # 1. 递归+上下界
        # 递归并引入上界，下界来判断是否有效的二叉搜索树
        def dfs(root, left, right):
            if not root:
                return True
            elif left < root.val < right:
                # 这里再分别以左右两个子节点分别判断
                return dfs(root.left, left, root.val) and dfs(root.right, root.val, right)
            # 每个节点如果超过这个范围，直接返回false
            else:
                return False
        return dfs(root, float('-inf'), float('inf'))

        # 2. 中序遍历非递归方式 还不想看懂
        # if not root:
        #     return True
        # prev = None
        # stack = []
        # # 二叉搜索树中序遍历非递归方式
        # while root or stack:
        #     while root:
        #         stack.append(root)
        #         root = root.left
        #     root = stack.pop()
        #     # 判断前一个节点是否大于等于当前节点，是则不是有效的搜索二叉树，返回False
        #     if prev and root.val <= prev.val:
        #         return False
        #     # 保存前一个节点
        #     prev = root
        #     root = root.right
        # return True


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([2, 1, 3], True),
        ([5, 1, 4, None, None, 3, 6], False),
        ([1], True),
        ([2, 2, 2], False),
        ([1, 1], False),
        ([5, 4, 6, None, None, 3, 7], False),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.isValidBST(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)

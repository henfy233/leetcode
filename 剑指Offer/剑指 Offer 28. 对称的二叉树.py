# -*- encoding: utf-8 -*-
'''
@File    :   剑指 Offer 28. 对称的二叉树.py
@Time    :   2022/04/29 10:16:11
@Author  :   henfy
@Diffi   :   Easy
@Version :   1.0

题目：https://leetcode-cn.com/problems/dui-cheng-de-er-cha-shu-lcof/
'''

# Definition for a binary tree node.


import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 不会
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def recur(L, R):
            if not L and not R:
                return True
            if not L or not R or L.val != R.val:
                return False
            return recur(L.left, R.right) and recur(L.right, R.left)

        if not root:
            return
        return recur(root.left, root.right)

# -*- encoding: utf-8 -*-
'''
@File    :   剑指 Offer 27. 二叉树的镜像.py
@Time    :   2022/04/27 01:13:46
@Author  :   henfy
@Diffi   :   Easy
@Version :   1.0

题目：https://leetcode-cn.com/study-plan/lcof/?progress=ik4k9cr
'''

# Definition for a binary tree node.


import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        # 不会
        # 递归法
        # if not root:
        #     return
        # tmp = root.left
        # root.left = self.mirrorTree(root.right)
        # root.right = self.mirrorTree(tmp)
        # return root

        # 辅助栈（或队列）
        if not root:
            return
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            node.left, node.right = node.right, node.left
        return root

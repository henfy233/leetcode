# -*- encoding: utf-8 -*-
'''
@File    :   1. 开幕式焰火.py
@Time    :   2021/09/25 15:08:25
@Author  :   henfy
@Diffi   :   Easy
@Version :   1.0

题目：https://leetcode-cn.com/contest/season/2021-fall/problems/sZ59z6/
'''

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def numColor(self, root: TreeNode) -> int:
        d = []
        p = root

        def dfs(p: TreeNode):
            # print('p',p)
            if not p:
                return
            # print('p.val',p.val)
            if p.val not in d:
                d.append(p.val)
            dfs(p.left)
            dfs(p.right)
        dfs(p)
        return len(d)

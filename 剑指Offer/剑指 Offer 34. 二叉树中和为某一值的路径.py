# -*- encoding: utf-8 -*-
'''
@File    :   剑指 Offer 34. 二叉树中和为某一值的路径.py
@Time    :   2022/05/20 01:17:24
@Author  :   henfy
@Diffi   :   Middle
@Method  :   搜索与回溯算法（中等）

题目：https://leetcode.cn/problems/er-cha-shu-zhong-he-wei-mou-yi-zhi-de-lu-jing-lcof/
'''
# Definition for a binary tree node.


from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        # 先序遍历 + 路径记录
        res, path = [], []

        def recur(root, tar):
            if not root:
                return
            path.append(root.val)
            tar -= root.val
            if tar == 0 and not root.left and not root.right:
                res.append(list(path))
            recur(root.left, tar)
            recur(root.right, tar)
            path.pop()
        recur(root, target)
        return res

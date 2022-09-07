# -*- encoding: utf-8 -*-
'''
@File    :   剑指 Offer 54. 二叉搜索树的第k大节点.py
@Time    :   2022/05/24 16:23:28
@Author  :   henfy
@Diffi   :   Easy
@Method  :   搜索与回溯算法（中等）

题目：https://leetcode.cn/problems/er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof/
'''
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        # 中序遍历 + 提前返回
        def dfs(root):
            if not root:
                return
            dfs(root.right)
            if self.k == 0:
                return
            self.k -= 1
            if self.k == 0:
                self.res = root.val
            dfs(root.left)

        self.k = k
        dfs(root)
        return self.res

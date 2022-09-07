# -*- encoding: utf-8 -*-
'''
@File    :   剑指 Offer 55 - I. 二叉树的深度.py
@Time    :   2022/05/24 18:44:26
@Author  :   henfy
@Diffi   :   Easy
@Method  :   搜索与回溯算法（中等）

题目：https://leetcode.cn/problems/er-cha-shu-de-shen-du-lcof/
'''

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # 自己写
        # self.ma = 0

        # def dfs(node, depth):
        #     if not node:
        #         return
        #     if depth > self.ma:
        #         self.ma = max(self.ma, depth)
        #     dfs(node.left, depth+1)
        #     dfs(node.right, depth+1)

        # dfs(root, 1)
        # return self.ma

        # 后序遍历（DFS）
        # if not root:
        #     return 0
        # return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

        # 层序遍历（BFS）
        if not root:
            return 0
        queue, res = [root], 0
        while queue:
            tmp = []
            for node in queue:
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            queue = tmp
            res += 1
        return res

# -*- encoding: utf-8 -*-
'''
@File    :   104. 二叉树的最大深度.py
@Time    :   2021/07/28 16:27:09
@Author  :   henfy
@Diffi   :   Easy
@Version :   1.0

题目：https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/
'''
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # 遇到树的问题，可以无脑优先考虑递归的方式
        # if not root:
        #     return 0
        # left = self.maxDepth(root.left)
        # right = self.maxDepth(root.right)
        # return max(left, right) + 1

        # 同上不同的写法
        return 0 if not root else max(self.maxDepth(root.left), self.maxDepth(root.right))+1

        # 自己写 数组元素用全局
        # maxDepth = [0]
        # def dfs(node, depth):
        #     if not node:
        #         return
        #     print('val', node.val)
        #     print('depth', depth)
        #     if depth > maxDepth[0]:
        #         maxDepth[0] = depth
        #     dfs(node.left, depth+1)
        #     dfs(node.right, depth+1)
        # dfs(root, 1)
        # return maxDepth[0]

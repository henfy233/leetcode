# -*- encoding: utf-8 -*-
'''
@File    :   剑指 Offer 55 - II. 平衡二叉树.py
@Time    :   2022/05/24 18:53:53
@Author  :   henfy
@Diffi   :   Easy
@Method  :   搜索与回溯算法（中等）

题目：https://leetcode.cn/problems/ping-heng-er-cha-shu-lcof/
'''

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 后序遍历 + 剪枝 （从底至顶）
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def recur(root):
            if not root:
                return 0
            left = recur(root.left)
            if left == -1:
                return -1
            right = recur(root.right)
            if right == -1:
                return -1
            return max(left, right) + 1 if abs(left - right) <= 1 else -1

        return recur(root) != -1


# 先序遍历 + 判断深度 （从顶至底）
# class Solution:
#     def isBalanced(self, root: TreeNode) -> bool:
#         if not root:
#             return True
#         return abs(self.depth(root.left) - self.depth(root.right)) <= 1 and \
#             self.isBalanced(root.left) and self.isBalanced(root.right)

#     def depth(self, root):
#         if not root:
#             return 0
#         return max(self.depth(root.left), self.depth(root.right)) + 1

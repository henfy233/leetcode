# -*- encoding: utf-8 -*-
'''
@File    :   剑指 Offer 68 - I. 二叉搜索树的最近公共祖先.py
@Time    :   2022/05/24 20:46:05
@Author  :   henfy
@Diffi   :   Easy
@Method  :   搜索与回溯算法（中等）

题目：https://leetcode.cn/problems/er-cha-sou-suo-shu-de-zui-jin-gong-gong-zu-xian-lcof/
'''

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 迭代
        # if p.val > q.val:
        #     p, q = q, p  # 保证 p.val < q.val
        # while root:
        #     if root.val < p.val:  # p,q 都在 root 的右子树中
        #         root = root.right  # 遍历至右子节点
        #     elif root.val > q.val:  # p,q 都在 root 的左子树中
        #         root = root.left  # 遍历至左子节点
        #     else:
        #         break
        # return root

        # 递归
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        return root

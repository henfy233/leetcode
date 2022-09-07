# -*- encoding: utf-8 -*-
'''
@File    :   剑指 Offer 07. 重建二叉树.py
@Time    :   2022/05/24 21:05:36
@Author  :   henfy
@Diffi   :   Middle
@Method  :   分治算法（中等）

题目：https://leetcode.cn/problems/zhong-jian-er-cha-shu-lcof/
'''

# Definition for a binary tree node.


from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

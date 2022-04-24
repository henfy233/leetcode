# -*- encoding: utf-8 -*-
'''
@File    :   653. 两数之和 IV - 输入 BST.py
@Time    :   2022/03/21 00:27:46
@Author  :   henfy
@Diffi   :   Easy
@Version :   1.0

题目：https://leetcode-cn.com/problems/two-sum-iv-input-is-a-bst/
'''

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:

# -*- encoding: utf-8 -*-
'''
@File    :   108. 将有序数组转换为二叉搜索树.py
@Time    :   2021/08/31 23:35:49
@Author  :   henfy
@Diffi   :   Easy
@Version :   1.0

题目：https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree/
'''

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        # return 0

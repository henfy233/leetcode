# -*- encoding: utf-8 -*-
'''
@File    :   98. 验证二叉搜索树.py
@Time    :   2021/07/29 23:39:01
@Author  :   henfy
@Diffi   :   Medium
@Version :   1.0

题目：https://leetcode-cn.com/problems/validate-binary-search-tree/
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # 1. 递归+上下界
        # 递归并引入上界，下界来判断是否有效的二叉搜索树
        def dfs(root, left, right):
            if not root:
                return True
            elif left < root.val < right:
                # 这里再分别以左右两个子节点分别判断
                return dfs(root.left, left, root.val) and dfs(root.right, root.val, right)
            # 每个节点如果超过这个范围，直接返回false
            else:
                return False
        return dfs(root, float('-inf'), float('inf'))

        # 2. 中序遍历非递归方式 还不想看懂
        # if not root:
        #     return True
        # prev = None
        # stack = []
        # # 二叉搜索树中序遍历非递归方式
        # while root or stack:
        #     while root:
        #         stack.append(root)
        #         root = root.left
        #     root = stack.pop()
        #     # 判断前一个节点是否大于等于当前节点，是则不是有效的搜索二叉树，返回False
        #     if prev and root.val <= prev.val:
        #         return False
        #     # 保存前一个节点
        #     prev = root
        #     root = root.right
        # return True

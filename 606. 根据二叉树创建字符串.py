# -*- encoding: utf-8 -*-
'''
@File    :   606. 根据二叉树创建字符串.py
@Time    :   2022/03/19 01:01:25
@Author  :   henfy
@Diffi   :   Easy
@Version :   1.0

题目：https://leetcode-cn.com/problems/construct-string-from-binary-tree/
'''

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        # 自己做
        # ans = []

        # def dfs(root):
        #     if not root:
        #         return
        #     print(root.val)
        #     ans.append(str(root.val))
        #     if not root.left and not root.right:
        #         return
        #     # else:
        #     ans.append('(')
        #     dfs(root.left)
        #     ans.append(')')
        #     if not root.right:
        #         return
        #     else:
        #         ans.append('(')
        #         dfs(root.right)
        #         ans.append(')')

        # dfs(root)
        # return ''.join(ans)

        # 递归
        if root is None:
            return ""
        if root.left is None and root.right is None:
            return str(root.val)
        if root.right is None:
            return f"{root.val}({self.tree2str(root.left)})"
        return f"{root.val}({self.tree2str(root.left)})({self.tree2str(root.right)})"

        # 迭代
        # ans = ""
        # st = [root]
        # vis = set()
        # while st:
        #     node = st[-1]
        #     if node in vis:
        #         if node != root:
        #             ans += ")"
        #         st.pop()
        #     else:
        #         vis.add(node)
        #         if node != root:
        #             ans += "("
        #         ans += str(node.val)
        #         if node.left is None and node.right:
        #             ans += "()"
        #         if node.right:
        #             st.append(node.right)
        #         if node.left:
        #             st.append(node.left)
        # return ans

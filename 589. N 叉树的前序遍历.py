# -*- encoding: utf-8 -*-
'''
@File    :   589. N 叉树的前序遍历.py
@Time    :   2022/03/10 00:26:15
@Author  :   henfy
@Diffi   :   Easy
@Version :   1.0

题目：https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal/
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""




from collections import defaultdict
from typing import List
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        # def dfs(root, ans):
        #     for i in range(len(root.children)):
        #         # print('i', i)
        #         # print('root.children[i]', root.children[i].val)
        #         # root = root.children[i]
        #         ans.append(root.children[i].val)
        #         dfs(root.children[i], ans)
        #     # print(root.children)

        # # print(root.children)
        # if not root:
        #     return []
        # ans = [root.val]
        # dfs(root, ans)
        # return ans

        # 递归
        # ans = []

        # def dfs(node: 'Node'):
        #     if node is None:
        #         return
        #     ans.append(node.val)
        #     for ch in node.children:
        #         dfs(ch)
        # dfs(root)
        # return ans

        # 迭代
        if root is None:
            return []
        ans = []
        st = []
        nextIndex = defaultdict(int)
        node = root
        while st or node:
            while node:
                ans.append(node.val)
                st.append(node)
                if not node.children:
                    break
                nextIndex[node] = 1
                node = node.children[0]
            node = st[-1]
            i = nextIndex[node]
            if i < len(node.children):
                nextIndex[node] = i + 1
                node = node.children[i]
            else:
                st.pop()
                del nextIndex[node]
                node = None
        return ans

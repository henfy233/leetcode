# -*- encoding: utf-8 -*-
'''
@File    :   590. N 叉树的后序遍历.py
@Time    :   2022/03/12 11:25:53
@Author  :   henfy
@Diffi   :   Easy
@Version :   1.0

题目：https://leetcode-cn.com/problems/n-ary-tree-postorder-traversal/
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""




from typing import List
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        # 通过，忘记注释输出print，超出输出限制
        # ans = []
        # if not root:
        #     return ans

        # def dfs(root):
        #     # print(len(root.children))
        #     # n = len(root.children)
        #     # if root is None:
        #     #     return
        #     for ch in root.children:
        #         dfs(ch)
        #     ans.append(root.val)
        #     # print('ans', ans)

        # dfs(root)
        # # ans.append(root.val)
        # return ans

        # 递归
        ans = []

        def dfs(node: 'Node'):
            if node is None:
                return
            for ch in node.children:
                dfs(ch)
            ans.append(node.val)
        dfs(root)
        return ans

        # 迭代
        # if root is None:
        #     return []
        # ans = []
        # st = []
        # nextIndex = defaultdict(int)
        # node = root
        # while st or node:
        #     while node:
        #         st.append(node)
        #         if not node.children:
        #             break
        #         nextIndex[node] = 1
        #         node = node.children[0]
        #     node = st[-1]
        #     i = nextIndex[node]
        #     if i < len(node.children):
        #         nextIndex[node] = i + 1
        #         node = node.children[i]
        #     else:
        #         ans.append(node.val)
        #         st.pop()
        #         del nextIndex[node]
        #         node = None
        # return ans

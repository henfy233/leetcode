# -*- encoding: utf-8 -*-
'''
@File    :   102. 二叉树的层序遍历.py
@Time    :   2021/07/31 18:31:22
@Author  :   henfy
@Diffi   :   Medium
@Version :   1.0

题目：https://leetcode-cn.com/problems/binary-tree-level-order-traversal/
'''

# Definition for a binary tree node.


from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # 1. DFS解决 自己做的
        # arr = []

        # def dfs(root, maxDepth):
        #     # 边界条件判断
        #     if not root:
        #         return
        #     # print('len(arr)', len(arr))
        #     # print('maxDepth', maxDepth)
        #     if len(arr) <= maxDepth:
        #         arr.append([])
        #     arr[maxDepth].append(root.val)
        #     dfs(root.left, maxDepth+1)
        #     dfs(root.right, maxDepth+1)
        # dfs(root, 0)
        # # print('arr', arr)
        # return arr
        # 执行用时：20 ms, 在所有 Python 提交中击败了74.96 % 的用户
        # 内存消耗：13.9 MB, 在所有 Python 提交中击败了5.95 % 的用户

        # 2. BFS解决
        # 边界条件判断
        if not root:
            return []
        # 队列 根节点入队
        queue = [root]
        res = []
        # 如果队列不为空就继续循环
        while queue:
            # BFS打印，length表示的是每层的结点数
            length = len(queue)
            # subList存储的是每层的结点值
            subList = []
            for _ in range(length):
                # 出队
                node = queue.pop(0)
                subList.append(node.val)
                # 左右子节点如果不为空就加入到队列中
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # 把每层的结点值存储在res中，
            res.append(subList)
        return res
        # 执行用时：20 ms, 在所有 Python 提交中击败了74.96 % 的用户
        # 内存消耗：13.1 MB, 在所有 Python 提交中击败了96.02 % 的用户

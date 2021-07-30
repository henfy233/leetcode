#
# @lc app=leetcode.cn id=863 lang=python
#
# [863] 二叉树中所有距离为 K 的结点
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from typing import Collection


class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        # 1. 深度优先搜索 + 哈希表
        # node_parent = {}

        # # dfs记录当前节点的父节点（完善邻接表）
        # def dfs_find_parent(node):
        #     if node:
        #         if node.left:
        #             node_parent[node.left] = node
        #         if node.right:
        #             node_parent[node.right] = node
        #         dfs_find_parent(node.left)
        #         dfs_find_parent(node.right)

        # dfs_find_parent(root)

        # # 从target节点开始结算步长
        # def dfs_find_res(node, prev, cur_dist):
        #     if node:
        #         print('val', node.val)
        #         print('cur_dist', cur_dist)
        #         if cur_dist == k:
        #             res.append(node.val)
        #             return
        #         if node.left != prev:
        #             dfs_find_res(node.left, node, cur_dist + 1)
        #         if node.right != prev:
        #             dfs_find_res(node.right, node, cur_dist + 1)
        #         if node in node_parent and node_parent[node] != prev:
        #             dfs_find_res(node_parent[node], node, cur_dist + 1)

        # res = []
        # dfs_find_res(target, None, 0)
        # return res

        # 2. 建图+bfs波纹法
        node_parent = {}
        # dfs记录当前节点的父节点（完善邻接表）

        def dfs_find_parent(node):
            if node:
                if node.left:
                    node_parent[node.left] = node
                if node.right:
                    node_parent[node.right] = node
                dfs_find_parent(node.left)
                dfs_find_parent(node.right)
        dfs_find_parent(root)
        node_parent = {}

        def dfs_find_parent(node):
            if node:
                if node.left:
                    node_parent[node.left] = node
                if node.right:
                    node_parent[node.right] = node
                dfs_find_parent(node.left)
                dfs_find_parent(node.right)
        dfs_find_parent(root)
        if k == 0:
            return [target.val]
        res = []
        Q = Collection.deque()
        visited = set()
        Q.append(target)
        visited.add(target)
        level = 0
        while Q and level < k:
            level += 1
            for _ in range(len(Q)):
                x = Q.popleft()
                for y in [node_parent[x] if x in node_parent else None, x.left, x.right]:
                    if y and y not in visited:
                        print('level', level)
                        print('val', y.val)
                        if level == k:
                            res.append(y.val)  # 先判
                        Q.append(y)
                        visited.add(y)
        return res


# @lc code=end

# -*- encoding: utf-8 -*-
'''
@File    :   430. 扁平化多级双向链表.py
@Time    :   2021/09/24 10:05:19
@Author  :   henfy
@Diffi   :   Medium
@Version :   1.0

题目：https://leetcode-cn.com/problems/flatten-a-multilevel-doubly-linked-list/
'''

# Definition for a Node.


class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        # 一看到题目就不会做了

        # 1. 深度优先搜索
        # https://leetcode-cn.com/problems/flatten-a-multilevel-doubly-linked-list/solution/bian-ping-hua-duo-ji-shuang-xiang-lian-b-383h/
        def dfs(node: "Node") -> "Node":
            cur = node
            # 记录链表的最后一个节点
            last = None

            while cur:
                nxt = cur.next
                # 如果有子节点，那么首先处理子节点
                if cur.child:
                    child_last = dfs(cur.child)

                    nxt = cur.next
                    # 将 node 与 child 相连
                    cur.next = cur.child
                    cur.child.prev = cur

                    # 如果 nxt 不为空，就将 last 与 nxt 相连
                    if nxt:
                        child_last.next = nxt
                        nxt.prev = child_last

                    # 将 child 置为空
                    cur.child = None
                    last = child_last
                else:
                    last = cur
                cur = nxt

            return last

        dfs(head)
        return head

# -*- encoding: utf-8 -*-
'''
@File    :   剑指 Offer 32 - III. 从上到下打印二叉树 III.py
@Time    :   2022/04/26 23:44:18
@Author  :   henfy
@Diffi   :   Middle
@Version :   1.0

题目：https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof/
'''

# Definition for a binary tree node.
import collections
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # 自己写，偷懒，直接最后倒序
        if not root:
            return []
        res, queue = [], collections.deque()
        seq = False
        queue.append(root)
        while queue:
            tmp = []
            seq = not seq
            for _ in range(len(queue)):
                node = queue.popleft()
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if seq:
                res.append(tmp)
            else:
                res.append(tmp[::-1])
        return res

        '''
        作者：jyd
        链接：https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof/solution/mian-shi-ti-32-iii-cong-shang-dao-xia-da-yin-er--3/
        来源：力扣（LeetCode）
        著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        '''
        # 层序遍历 + 双端队列
        # if not root:
        #     return []
        # res, deque = [], collections.deque([root])
        # while deque:
        #     tmp = collections.deque()
        #     for _ in range(len(deque)):
        #         node = deque.popleft()
        #         if len(res) % 2:
        #             tmp.appendleft(node.val)  # 偶数层 -> 队列头部
        #         else:
        #             tmp.append(node.val)  # 奇数层 -> 队列尾部
        #         if node.left:
        #             deque.append(node.left)
        #         if node.right:
        #             deque.append(node.right)
        #     res.append(list(tmp))
        # return res

        # 层序遍历 + 双端队列（奇偶层逻辑分离）
        # if not root:
        #     return []
        # res, deque = [], collections.deque()
        # deque.append(root)
        # while deque:
        #     tmp = []
        #     # 打印奇数层
        #     for _ in range(len(deque)):
        #         # 从左向右打印
        #         node = deque.popleft()
        #         tmp.append(node.val)
        #         # 先左后右加入下层节点
        #         if node.left:
        #             deque.append(node.left)
        #         if node.right:
        #             deque.append(node.right)
        #     res.append(tmp)
        #     if not deque:
        #         break  # 若为空则提前跳出
        #     # 打印偶数层
        #     tmp = []
        #     for _ in range(len(deque)):
        #         # 从右向左打印
        #         node = deque.pop()
        #         tmp.append(node.val)
        #         # 先右后左加入下层节点
        #         if node.right:
        #             deque.appendleft(node.right)
        #         if node.left:
        #             deque.appendleft(node.left)
        #     res.append(tmp)
        # return res

        # 层序遍历 + 倒序
        # if not root:
        #     return []
        # res, queue = [], collections.deque()
        # queue.append(root)
        # while queue:
        #     tmp = []
        #     for _ in range(len(queue)):
        #         node = queue.popleft()
        #         tmp.append(node.val)
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        #     res.append(tmp[::-1] if len(res) % 2 else tmp)
        # return res

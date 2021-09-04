# -*- encoding: utf-8 -*-
'''
@File    :   剑指 Offer 22. 链表中倒数第k个节点.py
@Time    :   2021/09/02 00:20:09
@Author  :   henfy
@Diffi   :   Easy
@Version :   1.0

题目：https://leetcode-cn.com/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof/
'''

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        # 自己写，之前做过，简单,用的双指针方法
        left = 1
        rNode = head
        while left < k:
            # print('rNode.val', rNode.val)
            rNode = rNode.next
            left += 1
        while rNode.next:
            head = head.next
            rNode = rNode.next
        return head
        # 执行用时：28 ms, 在所有 Python3 提交中击败了93.13 % 的用户
        # 内存消耗：15.1 MB, 在所有 Python3 提交中击败了5.37 % 的用户

        # 1. 顺序查找
        # https://leetcode-cn.com/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof/solution/lian-biao-zhong-dao-shu-di-kge-jie-dian-1pz9l/
        # node, n = head, 0
        # while node:
        #     node = node.next
        #     n += 1
        # node = head
        # for _ in range(n-k):
        #     node = node.next
        # return node
        # 时间复杂度：O(n)，其中 n 为链表的长度。需要两次遍历。
        # 空间复杂度：O(1)。

        # 2. 双指针
        # fast, slow = head, head
        # while fast and k > 0:
        #     fast, k = fast.next, k - 1
        # while fast:
        #     fast, slow = fast.next, slow.next
        # return slow
        # 时间复杂度：O(n)，其中 n 为链表的长度。我们使用快慢指针，只需要一次遍历即可，复杂度为 O(n)。
        # 空间复杂度：O(1)。

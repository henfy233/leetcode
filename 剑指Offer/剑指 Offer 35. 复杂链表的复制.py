# -*- encoding: utf-8 -*-
'''
@File    :   剑指 Offer 35. 复杂链表的复制.py
@Time    :   2022/04/21 16:49:50
@Author  :   henfy
@Diffi   :   Middle
@Version :   1.0

题目：https://leetcode-cn.com/problems/fu-za-lian-biao-de-fu-zhi-lcof/
'''
# Definition for a Node.


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        # 回溯 + 哈希表
        # if not head:
        #     return
        # dic = {}

        # cur = head
        # while cur:
        #     dic[cur] = Node(cur.val)
        #     cur = cur.next
        # cur = head

        # while cur:
        #     dic[cur].next = dic.get(cur.next)
        #     dic[cur].random = dic.get(cur.random)
        #     cur = cur.next
        # return dic[head]

        # 迭代 + 节点拆分
        if not head:
            return
        cur = head
        # 1. 复制各节点，并构建拼接链表
        while cur:
            tmp = Node(cur.val)
            tmp.next = cur.next
            cur.next = tmp
            cur = tmp.next
        # 2. 构建各新节点的 random 指向
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        # 3. 拆分两链表
        cur = res = head.next
        pre = head
        while cur.next:
            pre.next = pre.next.next
            cur.next = cur.next.next
            pre = pre.next
            cur = cur.next
        pre.next = None  # 单独处理原链表尾节点
        return res      # 返回新链表头节点


# 作者：jyd
# 链接：https://leetcode-cn.com/problems/fu-za-lian-biao-de-fu-zhi-lcof/solution/jian-zhi-offer-35-fu-za-lian-biao-de-fu-zhi-ha-xi-/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

#
# @lc app=leetcode.cn id=138 lang=python
#
# [138] 复制带随机指针的链表
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        # 1. 回溯 + 哈希表
        if not head:
            return None
        # 创建一个哈希表，key是原节点，value是新节点
        d = dict()
        p = head
        # 将原节点和新节点放入哈希表中
        while p:
            new_node = Node(p.val, None, None)
            d[p] = new_node
            p = p.next
        p = head
        # 遍历原链表，设置新节点的next和random
        while p:
            # p是原节点，d[p]是对应的新节点，p.next是原节点的下一个
            # d[p.next]是原节点下一个对应的新节点
            if p.next:
                d[p].next = d[p.next]
            # p.random是原节点随机指向
            # d[p.random]是原节点随机指向  对应的新节点
            if p.random:
                d[p].random = d[p.random]
            p = p.next
        # 返回头结点，即原节点对应的value(新节点)
        return d[head]

        # 2. 迭代 + 节点拆分
        # if not head:
        #     return None
        # # 第一步，在每个原节点后面创建一个新节点
        # # 1 -> 1'->2->2' -> 3 -> 3'
        # p = head
        # while p:
        #     new_node = Node(p.val, None, None)
        #     new_node.next = p.next
        #     p.next = new_node
        #     p = new_node.next
        # # 第二步，设置新节点的随机节点
        # p = head
        # while p:
        #     if p.random:
        #         p.next.random = p.random.next
        #     p = p.next.next
        # # 第三步，将两个链表分离
        # p = head
        # dummy = Node(-1, None, None)
        # cur = dummy
        # while p:
        #     cur.next = p.next
        #     cur = cur.next
        #     p.next = cur.next
        #     p = p.next
        # return dummy.next

# @lc code=end

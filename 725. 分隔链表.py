# -*- encoding: utf-8 -*-
'''
@File    :   725. 分隔链表.py
@Time    :   2021/09/22 15:36:16
@Author  :   henfy
@Diffi   :   Medium
@Version :   1.0

题目：https://leetcode-cn.com/problems/split-linked-list-in-parts/
'''
# Definition for singly-linked list.


from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitListToParts(self, head: ListNode, k: int) -> List[ListNode]:
        # 自己写，做不出
        # res = []
        # n = 0
        # p = head
        # while p:
        #     # print(p.val)
        #     # res.append(head)
        #     n += 1
        #     p = p.next
        # print('n', n)
        # weight = n//k
        # num = n % k
        # print('weight', weight)
        # print('num', num)
        # tmp = head
        # for i in range(num):
        #     x = 0
        #     node = ListNode()
        #     p = node
        #     while x < weight+1:
        #         print('tmp.val', tmp.val)
        #         p.val = tmp.val
        #         p = p.next
        #         tmp = tmp.next
        #         x += 1
        #     res.append(node)
        # for i in range(k-num):
        #     x = 0
        #     node = ListNode()
        #     p = node
        #     while x < weight:
        #         print('tmp.val', tmp.val)
        #         p.val = tmp.val
        #         p = p.next
        #         tmp = tmp.next
        #         x += 1
        #     res.append(node)
        # # print('res',res)
        # return res

        # 1. 拆分链表 与下面方法类似
        # https://leetcode-cn.com/problems/split-linked-list-in-parts/solution/fen-ge-lian-biao-by-leetcode-solution-wevt/
        # n = 0
        # temp = head
        # while temp != None:
        #     n += 1
        #     temp = temp.next
        # quotient = n // k
        # remainder = n % k
        # parts = [None for _ in range(k)]
        # print('parts', parts)
        # curr = head
        # for i in range(k):
        #     if curr != None:
        #         parts[i] = curr
        #         partSize = quotient + (1 if i < remainder else 0)
        #         print('partSize', partSize)
        #         for j in range(1, partSize):
        #             curr = curr.next
        #         next = curr.next
        #         curr.next = None
        #         curr = next
        # print('parts', parts)
        # return parts

        # 2. 模拟
        # https://leetcode-cn.com/problems/split-linked-list-in-parts/solution/cpython3java-1mo-ni-by-hanxin_hanxin-4ncy/
        # ----链表的长度
        n = 0
        p = head
        while p:
            n += 1
            p = p.next
        # ----每个分段的长度
        aver_sub_n = n // k  # ----平均每段的长度
        pre_long_n = n - aver_sub_n * k  # ----偏长的几段，放在前面
        # ----切分
        res = [None for _ in range(k)]
        p = head
        for i in range(k):
            # ----如果已经是空结点了，就break
            if p == None:
                break
            # ----划分给当前段平均长度
            cur_n = aver_sub_n + (1 if i < pre_long_n else 0)
            res[i] = p  # 当前段的段头，入res
            for _ in range(0, cur_n - 1, 1):
                p = p.next
            if p:
                p_nxt = p.next
                p.next = None
                p = p_nxt
        return res

        # 3. 边遍历边剪切
        # https://leetcode-cn.com/problems/split-linked-list-in-parts/solution/python3-bian-bian-li-bian-jian-qie-by-zh-v19b/
        # length = 0
        # temp = head
        # while temp != None:
        #     length += 1
        #     temp = temp.next

        # ans = [None for _ in range(k)]
        # curr = head
        # i = 0
        # while k >= 1 and curr != None:
        #     now = curr
        #     currLen = ceil(length / k)
        #     for _ in range(currLen-1):
        #         if curr != None:
        #             curr = curr.next
        #     if curr == None:
        #         break
        #     nxt = curr.next
        #     curr.next = None
        #     ans[i] = now
        #     curr = nxt
        #     k -= 1
        #     i += 1
        #     length -= currLen
        # return ans

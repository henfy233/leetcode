# -*- encoding: utf-8 -*-
'''
@File    :   剑指 Offer 41. 数据流中的中位数.py
@Time    :   2022/05/24 18:03:02
@Author  :   henfy
@Diffi   :   Hard
@Method  :   排序（中等）

题目：https://leetcode.cn/problems/shu-ju-liu-zhong-de-zhong-wei-shu-lcof/
'''

# 优先队列 / 堆
from heapq import *


class MedianFinder:
    def __init__(self):
        self.A = []  # 小顶堆，保存较大的一半
        self.B = []  # 大顶堆，保存较小的一半

    def addNum(self, num: int) -> None:
        if len(self.A) != len(self.B):
            heappush(self.A, num)
            heappush(self.B, -heappop(self.A))
        else:
            heappush(self.B, -num)
            heappush(self.A, -heappop(self.B))

    def findMedian(self) -> float:
        return self.A[0] if len(self.A) != len(self.B) else (self.A[0] - self.B[0]) / 2.0

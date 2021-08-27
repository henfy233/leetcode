# -*- encoding: utf-8 -*-
'''
@File    :   155. 最小栈.py
@Time    :   2021/08/04 16:08:35
@Author  :   henfy
@Diffi   :   Easy
@Version :   1.0

题目：https://leetcode-cn.com/problems/min-stack/
'''


class MinStack(object):
    nums = []

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []

    # 将元素 x 推入栈中。
    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.nums.append(val)

    # 删除栈顶的元素。
    def pop(self):
        """
        :rtype: None
        """
        return self.nums.pop()

    # 获取栈顶元素。
    def top(self):
        """
        :rtype: int
        """
        return self.nums[-1]

    # 检索栈中的最小元素。
    def getMin(self):
        """
        :rtype: int
        """
        return min(self.nums)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

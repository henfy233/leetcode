# -*- encoding: utf-8 -*-
'''
@File    :   剑指 Offer 09. 用两个栈实现队列.py
@Time    :   2022/04/20 00:51:03
@Author  :   henfy
@Diffi   :   Easy
@Version :   1.0

题目：https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof/
'''
# 不会


class CQueue:

    def __init__(self):
        self.head, self.tail = [], []

    def appendTail(self, value: int) -> None:
        self.head.append(value)

    def deleteHead(self) -> int:
        if len(self.tail) == 0:
            if len(self.head) == 0:
                return -1
            self.in2out()
        return self.tail.pop()

    def in2out(self):
        while(len(self.head) != 0):
            self.tail.append(self.head.pop())

    # def deleteHead(self) -> int:
    #     if not self.stack2:
    #         while self.stack1:
    #             self.stack2.append(self.stack1.pop())
    #     return self.stack2.pop() if self.stack2 else -1

# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()

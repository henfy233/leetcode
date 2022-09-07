# -*- encoding: utf-8 -*-
'''
@File    :   剑指 Offer 64. 求1+2+…+n.py
@Time    :   2022/05/24 20:33:19
@Author  :   henfy
@Diffi   :   Middle
@Method  :   搜索与回溯算法（中等）

题目：https://leetcode.cn/problems/qiu-12n-lcof/
'''


# class Solution:
#     def sumNums(self, n: int) -> int:
#         # 平均计算
#         return (1+n)*n//2

#         # 迭代
#         res = 0
#         for i in range(1, n + 1):
#             res += i
#         return res

#         # 递归
#         if n == 1:
#             return 1
#         n += self.sumNums(n - 1)
#         return n


class Solution:
    def __init__(self):
        self.res = 0

    def sumNums(self, n: int) -> int:
        n > 1 and self.sumNums(n - 1)
        self.res += n
        return self.res


if __name__ == '__main__':
    s = Solution()
    test_list = [
        (3, 6),
        (9, 45),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.sumNums(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)

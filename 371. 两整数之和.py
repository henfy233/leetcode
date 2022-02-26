# -*- encoding: utf-8 -*-
'''
@File    :   371. 两整数之和.py
@Time    :   2021/09/26 10:23:12
@Author  :   henfy
@Diffi   :   Medium
@Version :   1.0

题目：https://leetcode-cn.com/problems/sum-of-two-integers/
'''


class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 自己写，系统检测不出来
        return ((a << 1) + (b << 1))//2


if __name__ == '__main__':
    s = Solution()
    test_list = [
        (1, 2, 3),
        (2, 3, 5),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.getSum(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)

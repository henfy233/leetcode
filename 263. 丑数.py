# -*- encoding: utf-8 -*-
'''
@File    :   263. 丑数.py
@Time    :   2021/08/09 10:58:59
@Author  :   henfy
@Diffi   :   Easy
@Version :   1.0

题目：https://leetcode-cn.com/problems/ugly-number
'''


class Solution(object):
    def isUgly(self, n: int) -> bool:
        # 自己写，不太懂里面规则，看答案吧
        # if n == 1 or n == 2:
        #     return True
        # elif n <= 0:
        #     return False
        # if n % 3 == 0 or n % 5 == 0:
        #     return True
        # elif n % 2 == 0 and n//2 % 2 == 0:
        #     return True
        # else:
        #     return False

        # 1. 数字
        # 根据丑数的定义，0 和负整数一定不是丑数。
        # 当 n > 0 时，若 n 是丑数，则 n 可以写成 n = 2 ^ a × 3 ^ b × 5 ^ c 的形式，其中 a, b, c 都是非负整数。特别地，当 a, b, c 都是 0 时，n = 1。
        # 为判断 n 是否满足上述形式，可以对 n 反复除以 2, 3, 5，直到 n 不再包含质因数 2, 3, 5。若剩下的数等于 1，则说明 n 不包含其他质因数，是丑数；否则，说明 n 包含其他质因数，不是丑数。
        if n <= 0:
            return False
        factors = [2, 3, 5]
        for factor in factors:
            while n % factor == 0:
                n //= factor
        return n == 1
        # 复杂度分析
        # 时间复杂度：O(logn)。时间复杂度取决于对 n 除以 2, 3, 5 的次数，由于每次至少将 n 除以 2，因此除法运算的次数不会超过 O(logn)。
        # 空间复杂度：O(1)。
        # 执行用时：20 ms, 在所有 Python 提交中击败了93.01 % 的用户
        # 内存消耗：12.9 MB, 在所有 Python 提交中击败了65.07 % 的用户


if __name__ == '__main__':
    s = Solution()
    test_list = [
        (6, True),
        (8, True),
        (14, False),
        (1, True),
        (-2147483648, False),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.isUgly(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)

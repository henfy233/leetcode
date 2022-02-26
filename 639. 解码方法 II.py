# -*- encoding: utf-8 -*-
'''
@File    :   639. 解码方法 II.py
@Time    :   2021/09/28 00:18:52
@Author  :   henfy
@Diffi   :   Hard
@Version :   1.0

题目：https://leetcode-cn.com/problems/decode-ways-ii/
'''


class Solution:
    def numDecodings(self, s: str) -> int:
        # 1. 动态规划
        # https://leetcode-cn.com/problems/decode-ways-ii/solution/jie-ma-fang-fa-ii-by-leetcode-solution-23af/
        mod = 10**9 + 7

        def check1digit(ch: str) -> int:
            if ch == "0":
                return 0
            return 9 if ch == "*" else 1

        def check2digits(c0: str, c1: str) -> int:
            if c0 == c1 == "*":
                return 15
            if c0 == "*":
                return 2 if c1 <= "6" else 1
            if c1 == "*":
                return 9 if c0 == "1" else (6 if c0 == "2" else 0)
            return int(c0 != "0" and int(c0) * 10 + int(c1) <= 26)

        n = len(s)
        # a = f[i-2], b = f[i-1], c = f[i]
        a, b, c = 0, 1, 0
        for i in range(1, n + 1):
            c = b * check1digit(s[i - 1])
            if i > 1:
                c += a * check2digits(s[i - 2], s[i - 1])
            c %= mod
            a = b
            b = c

        return c


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ("*", 9),
        ("1*", 18),
        ("2*", 15),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.numDecodings(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)

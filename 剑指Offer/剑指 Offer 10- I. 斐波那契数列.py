# -*- encoding: utf-8 -*-
'''
@File    :   剑指 Offer 10- I. 斐波那契数列.py
@Time    :   2021/09/04 00:23:44
@Author  :   henfy
@Diffi   :   Easy
@Version :   1.0

题目：https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof/
'''


from typing import List


class Solution:
    def fib(self, n: int) -> int:
        # 自己写，之前做过，数组存储信息
        # ans = [0]*(n+1)
        # if n == 0:
        #     return 0
        # if n == 1:
        #     return 1
        # ans[0] = 0
        # ans[1] = 1
        # for i in range(2, n+1):
        #     ans[i] = ans[i-1] + ans[i-2]
        # return ans[n] % 1000000007
        # 执行用时：44 ms, 在所有 Python3 提交中击败了15.41 % 的用户
        # 内存消耗：14.9 MB, 在所有 Python3 提交中击败了48.64 % 的用户

        # 自己写，省空间，用变量存
        if n == 0:
            return 0
        if n == 1:
            return 1
        min = 0
        middle = 1
        for i in range(2, n+1):
            max = middle + min
            min = middle
            middle = max
        return middle % 1000000007
        # 执行用时：32 ms, 在所有 Python3 提交中击败了73.81 % 的用户
        # 内存消耗：15 MB, 在所有 Python3 提交中击败了26.50 % 的用户

        # 1. 动态规划
        # https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof/solution/fei-bo-na-qi-shu-lie-by-leetcode-solutio-hbss/
        # MOD = 10 ** 9 + 7
        # if n < 2:
        #     return n
        # p, q, r = 0, 0, 1
        # for _ in range(2, n + 1):
        #     p = q
        #     q = r
        #     r = (p + q) % MOD
        # return r
        # 时间复杂度：O(n)。
        # 空间复杂度：O(1)。

        # 2. 矩阵快速幂
        # https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof/solution/fei-bo-na-qi-shu-lie-by-leetcode-solutio-hbss/
        # MOD = 10 ** 9 + 7
        # if n < 2:
        #     return n

        # def multiply(a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
        #     c = [[0, 0], [0, 0]]
        #     for i in range(2):
        #         for j in range(2):
        #             c[i][j] = (a[i][0] * b[0][j] + a[i][1] * b[1][j]) % MOD
        #     return c

        # def matrix_pow(a: List[List[int]], n: int) -> List[List[int]]:
        #     ret = [[1, 0], [0, 1]]
        #     while n > 0:
        #         if n & 1:
        #             ret = multiply(ret, a)
        #         n >>= 1
        #         a = multiply(a, a)
        #     return ret

        # res = matrix_pow([[1, 1], [1, 0]], n - 1)
        # return res[0][0]
        # 时间复杂度：O(logn)。
        # 空间复杂度：O(1)。


if __name__ == '__main__':
    s = Solution()
    test_list = [
        (2, 1),
        (5, 5),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.fib(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)

#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   1137. 第 N 个泰波那契数.py
@Time    :   2021/08/08 10:14:43
@Author  :   henfy
@Diffi   :   easy
@Version :   1.0
'''

# here put the import lib


class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 自己写，这道题用数组存储，也可用三个数存储
        # if n < 3:
        #     arr = [0]*3
        # else:
        #     arr = [0]*(n+1)
        # arr[0] = 0
        # arr[1] = 1
        # arr[2] = 1
        # for i in range(3, n+1):
        #     arr[i] = arr[i-1]+arr[i-2]+arr[i-3]
        # return arr[n]
        # 执行用时：20 ms, 在所有 Python 提交中击败了32.61 % 的用户
        # 内存消耗：13.1 MB, 在所有 Python 提交中击败了13.75 % 的用户

        # 1.动态规划 用三个数省空间
        # 泰波那契数的边界条件是 T(0) = 0, T(1) = 1, T(2) = 1。当 n > 2 时，每一项的和都等于前三项的和，因此有如下递推关系：T(n) = T(n−1)+T(n−2)+T(n−3)
        # 由于泰波那契数存在递推关系，因此可以使用动态规划求解。动态规划的状态转移方程即为上述递推关系，边界条件为 T(0)、T(1) 和 T(2)。
        # 根据状态转移方程和边界条件，可以得到时间复杂度和空间复杂度都是 O(n) 的实现。由于 T(n) 只和前三项有关，因此可以使用「滚动数组思想」将空间复杂度优化成 O(1)。如下的代码中给出的就是这种实现。
        # if n == 0:
        #     return 0
        # if n <= 2:
        #     return 1
        # p = 0
        # q = r = 1
        # for _ in range(3, n + 1):
        #     s = p + q + r
        #     p, q, r = q, r, s
        # return s
        # 复杂度分析
        # 时间复杂度：O(n)。
        # 空间复杂度：O(1)。
        # 执行用时：8 ms, 在所有 Python 提交中击败了97.57 % 的用户
        # 内存消耗：13.2 MB, 在所有 Python 提交中击败了5.12 % 的用户

        # 2. 矩阵快速幂 还不理解
        # 方法一的时间复杂度是 O(n)。使用矩阵快速幂的方法可以降低时间复杂度。首先我们可以构建这样一个递推关系：
        # 因此只要我们能快速计算矩阵 M 的 n 次幂，就可以得到 T(n) 的值。如果直接求取 M ^ n，时间复杂度是 O(n)，可以定义矩阵乘法，然后用快速幂算法来加速这里 M ^ n的求取。
        if n == 0:
            return 0
        if n <= 2:
            return 1

        def multiply(a, b):
            c = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            for i in range(3):
                for j in range(3):
                    c[i][j] = a[i][0] * b[0][j] + \
                        a[i][1] * b[1][j] + a[i][2] * b[2][j]
            return c

        def matrix_pow(a, n):
            ret = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
            while n > 0:
                if n & 1:
                    ret = multiply(ret, a)
                n >>= 1
                a = multiply(a, a)
            return ret

        q = [[1, 1, 1], [1, 0, 0], [0, 1, 0]]
        res = matrix_pow(q, n)
        return res[0][2]
        # 复杂度分析
        # 时间复杂度：O(logn)。
        # 空间复杂度：O(1)。


if __name__ == '__main__':
    s = Solution()
    test_list = [
        (0, 0),
        (4, 4),
        (25, 1389537),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.tribonacci(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)

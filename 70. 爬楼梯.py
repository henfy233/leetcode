# -*- encoding: utf-8 -*-
'''
@File    :   70. 爬楼梯.py
@Time    :   2021/08/29 01:35:43
@Author  :   henfy
@Diffi   :   Easy
@Version :   1.0

题目：https://leetcode-cn.com/problems/climbing-stairs/
'''


from typing import List


# 这道题有递归、记忆化递归、动态规划做法
# https://leetcode-cn.com/problems/climbing-stairs/solution/pa-lou-ti-by-leetcode-solution/
class Solution:
    # @functools.lru_cache(100)  # 缓存装饰器
    def climbStairs(self, n: int) -> int:
        # 自己写，对动规不熟，还要再做
        # dp = [1]*(n+1)
        # if n == 1:
        #     return 1
        # # print(dp)
        # dp[2] = 2
        # for i in range(3, n+1):
        #     dp[i] = dp[i-1] + dp[i-2]
        # return dp[n]
        # 执行用时：28 ms, 在所有 Python3 提交中击败了88.74 % 的用户
        # 内存消耗：15 MB, 在所有 Python3 提交中击败了25.27 % 的用户

        # 1. 递归
        # 直接递归解法，容易超时，python可以加个缓存装饰器，这样也算是将递归转换成迭代的形式了
        # if n == 1:
        #     return 1
        # if n == 2:
        #     return 2
        # return self.climbStairs(n-1) + self.climbStairs(n-2)
        # 时间复杂度：O(2 ^ n)。
        # 空间复杂度：O(n)。

        # 2. 记忆化递归
        #     memo = [0]*(n+1)
        #     return self.climbStairsMemo(n, memo)

        # def climbStairsMemo(self, n: int, memo: List[int]) -> int:
        #     if memo[n] > 0:
        #         return memo[n]
        #     if n == 1:
        #         memo[n] = 1
        #     elif n == 2:
        #         memo[n] = 2
        #     else:
        #         memo[n] = self.climbStairsMemo(
        #             n-1, memo) + self.climbStairsMemo(n-2, memo)
        #     return memo[n]
        # 时间复杂度：O(n)。
        # 空间复杂度：O(n)。

        # 3. 动态规划
        # dp = [1]*(n+1)
        # if n == 1:
        #     return 1
        # dp[2] = 2
        # for i in range(3, n+1):
        #     dp[i] = dp[i-1] + dp[i-2]
        # return dp[n]
        # 时间复杂度：O(n)。
        # 空间复杂度：O(n)。

        # 4. 优化动态规划 滚动数组
        # if n == 1:
        #     return 1
        # first, second = 1, 2
        # for _ in range(3, n+1):
        #     third = first + second
        #     first = second
        #     second = third
        # return second
        # 时间复杂度：循环执行 n 次，每次花费常数的时间代价，故渐进时间复杂度为 O(n)。
        # 空间复杂度：这里只用了常数个变量作为辅助空间，故渐进空间复杂度为 O(1)。

        # 5. 矩阵快速幂

        # 6. 通项公式 如下
        # https://leetcode-cn.com/problems/climbing-stairs/solution/pa-lou-ti-by-leetcode-solution/
        import math
        sqrt5 = math.sqrt(5)
        fibn = math.pow((1 + sqrt5) / 2, n + 1) - \
            math.pow((1 - sqrt5) / 2, n + 1)
        return int(round(fibn / sqrt5))

        # 斐波那契数列的计算公式
        # https://leetcode-cn.com/problems/climbing-stairs/solution/70zhong-quan-chu-ji-python3hui-ji-liao-ti-jie-qu-w/
        # import math
        # sqrt5 = 5**0.5
        # fibin = math.pow((1+sqrt5)/2, n+1)-math.pow((1-sqrt5)/2, n+1)
        # return int(fibin/sqrt5)

        # 面向测试用例编程
        # https://leetcode-cn.com/problems/climbing-stairs/solution/70zhong-quan-chu-ji-python3hui-ji-liao-ti-jie-qu-w/
        # a = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946,
        # 17711, 28657,46368, 75025, 121393, 196418, 317811, 514229, 832040,1346269, 2178309, 3524578,
        # 5702887, 9227465, 14930352, 24157817, 39088169, 63245986, 102334155, 165580141, 267914296,
        # 433494437, 701408733, 1134903170, 1836311903]
        # return a[n-1]


if __name__ == '__main__':
    s = Solution()
    test_list = [
        (1, 1),
        (2, 2),
        (3, 3),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.climbStairs(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)

#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   313. 超级丑数.py
@Time    :   2021/08/09 10:49:47
@Author  :   henfy
@Diffi   :   middle
@Version :   1.0
'''

# here put the import lib


class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        # 参考了264题目的动规，自己理解写的，这种方法不错
        dp = [0] * (n + 1)
        dp[1] = 1
        np = len(primes)
        arr = [0]*np
        count = [1]*np
        for i in range(2, n + 1):
            for j in range(np):
                arr[j] = dp[count[j]]*primes[j]
            dp[i] = min(arr)
            for j in range(np):
                if dp[i] == arr[j]:
                    count[j] += 1
        return dp[n]
        # 执行用时：404 ms, 在所有 Python 提交中击败了95.24 % 的用户
        # 内存消耗：18.7 MB, 在所有 Python 提交中击败了76.19 % 的用户

        # 1. 最小堆
        # import heapq
        # seen = {1}
        # heap = [1]
        # for _ in range(n):
        #     ugly = heapq.heappop(heap)
        #     for prime in primes:
        #         nxt = ugly * prime
        #         if nxt not in seen:
        #             seen.add(nxt)
        #             heapq.heappush(heap, nxt)
        # return ugly
        # 复杂度分析
        # 时间复杂度：O(nmlognm)，其中 n 是待求的超级丑数的编号，m 是数组 primes 的长度。得到第 n 个超级丑数需要进行 n 次循环，每次循环都要从最小堆中取出 1 个元素以及向最小堆中加入最多 m 个元素，因此每次循环的时间复杂度是 O(lognm+mlognm) = O(mlognm)，总时间复杂度是 O(nmlognm)。
        # 空间复杂度：O(nm)，其中 n 是待求的超级丑数的编号，m 是数组 primes 的长度。空间复杂度主要取决于最小堆和哈希集合的大小，最小堆和哈希集合的大小都不会超过 nm。
        # 执行用时：1496 ms, 在所有 Python 提交中击败了38.09 % 的用户
        # 内存消耗：84.9 MB, 在所有 Python 提交中击败了32.14 % 的用户

        # 2. 动态规划
        # 方法一使用最小堆，会预先存储较多的超级丑数，导致空间复杂度较高，维护最小堆的过程也导致时间复杂度较高。可以使用动态规划的方法进行优化。
        # 定义数组 dp，其中 dp[i] 表示第 i 个超级丑数，第 n 个超级丑数即为 dp[n]。
        # 由于最小的超级丑数是 1，因此 dp[1] = 1。
        # 如何得到其余的超级丑数呢？创建与数组 primes 相同长度的数组 pointers，表示下一个超级丑数是当前指针指向的超级丑数乘以对应的质因数。初始时，数组 pointers 的元素值都是 1。
        # dp = [0] * (n + 1)
        # dp[1] = 1
        # m = len(primes)
        # pointers = [1] * m
        # for i in range(2, n + 1):
        #     min_num = min(dp[pointers[j]] * primes[j] for j in range(m))
        #     dp[i] = min_num
        #     for j in range(m):
        #         if dp[pointers[j]] * primes[j] == min_num:
        #             pointers[j] += 1
        # return dp[n]
        # 复杂度分析
        # 时间复杂度：O(nm)，其中 n 是待求的超级丑数的编号，m 是数组 primes 的长度。需要计算数组 dp 中的 n 个元素，每个元素的计算都需要 O(m) 的时间。
        # 空间复杂度：O(n+m)，其中 n 是待求的超级丑数的编号，m 是数组 primes 的长度。需要创建数组 dp 和数组 pointers，空间分别是 O(n) 和 O(m)。
        # 执行用时：508 ms, 在所有 Python 提交中击败了83.33 % 的用户
        # 内存消耗：18.7 MB, 在所有 Python 提交中击败了66.67 % 的用户


if __name__ == '__main__':
    s = Solution()
    test_list = [
        (12, [2, 7, 13, 19], 32),
        (1, [2, 3, 5], 1),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.nthSuperUglyNumber(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)

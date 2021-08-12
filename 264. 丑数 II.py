#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   264. 丑数 II.py
@Time    :   2021/08/09 11:20:52
@Author  :   henfy
@Diffi   :   middle
@Version :   1.0

给你一个整数 n ，请你找出并返回第 n 个 丑数 。
丑数 就是只包含质因数 2、3 和/或 5 的正整数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ugly-number-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib


class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 自己写，超出时间限制，过程没错
        # count = 0
        # factors = [2, 3, 5]
        # i = 1
        # while count < n:
        #     tmp = i
        #     for factor in factors:
        #         while tmp % factor == 0:
        #             tmp //= factor
        #     if tmp == 1:
        #         count += 1
        #     i += 1
        # return i-1

        # 1. 最小堆
        # 要得到从小到大的第 n 个丑数，可以使用最小堆实现。
        # 初始时堆为空。首先将最小的丑数 1 加入堆。
        # 每次取出堆顶元素 x，则 x 是堆中最小的丑数，由于 2x, 3x, 5x 也是丑数，因此将 2x, 3x, 5x 加入堆。
        # 上述做法会导致堆中出现重复元素的情况。为了避免重复元素，可以使用哈希集合去重，避免相同元素多次加入堆。
        # 在排除重复元素的情况下，第 n 次从最小堆中取出的元素即为第 n 个丑数。
        # import heapq
        # factors = [2, 3, 5]
        # seen = {1}
        # heap = [1]
        # for _ in range(n - 1):
        #     curr = heapq.heappop(heap)
        #     for factor in factors:
        #         nxt = curr * factor
        #         if nxt not in seen:
        #             seen.add(nxt)
        #             heapq.heappush(heap, nxt)
        # return heapq.heappop(heap)
        # 复杂度分析
        # 时间复杂度：O(nlogn)。得到第 n 个丑数需要进行 n 次循环，每次循环都要从最小堆中取出 1 个元素以及向最小堆中加入最多 3 个元素，因此每次循环的时间复杂度是 O(log3n+3*log3n) = O(logn)，总时间复杂度是 O(nlogn)。
        # 空间复杂度：O(n)。空间复杂度主要取决于最小堆和哈希集合的大小，最小堆和哈希集合的大小都不会超过 3n。

        # 2. 动态规划
        dp = [0] * (n + 1)
        dp[1] = 1
        p2 = p3 = p5 = 1
        for i in range(2, n + 1):
            num2, num3, num5 = dp[p2] * 2, dp[p3] * 3, dp[p5] * 5
            dp[i] = min(num2, num3, num5)
            if dp[i] == num2:
                p2 += 1
            if dp[i] == num3:
                p3 += 1
            if dp[i] == num5:
                p5 += 1
        return dp[n]
        # 复杂度分析
        # 时间复杂度：O(n)。需要计算数组 dp 中的 n 个元素，每个元素的计算都可以在 O(1) 的时间内完成。
        # 空间复杂度：O(n)。空间复杂度主要取决于数组 dp 的大小。
        # 执行用时：76 ms, 在所有 Python 提交中击败了91.71 % 的用户
        # 内存消耗：12.9 MB, 在所有 Python 提交中击败了95.85 % 的用户


if __name__ == '__main__':
    s = Solution()
    test_list = [
        (10, 12),
        (1, 1),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.nthUglyNumber(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)

# -*- encoding: utf-8 -*-
'''
@File    :   446. 等差数列划分 II - 子序列.py
@Time    :   2021/08/11 02:24:28
@Author  :   henfy
@Diffi   :   Hard
@Version :   1.0

题目：https://leetcode-cn.com/problems/arithmetic-slices-ii-subsequence
'''

# here put the import lib


# 最近忙，参考413题的做法，但还需优化写法
import collections


class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # n = len(nums)
        # if n == 1:
        #     return 0
        # d, t = nums[0] - nums[1], 0
        # ans = 0
        # for i in range(2, n):
        #     if nums[i-1] - nums[i] == d:
        #         t += 1
        #     else:
        #         d = nums[i-1]+nums[i]
        #         t = 0
        #     ans += t
        # return ans

        # 评论答案 和下面答案一致
        # N = len(A)
        # num = 0     # 总的等差数列的个数
        # # 等差数列个数数组
        # # 第 n 个元素最后的数为 A[n] 的等差数列的一个映射表
        # #   映射表的每一个元素表示公差为key的等差数列的个数 （尾数为A[n]）
        # # 注意： 此处的等差数列包含仅有两个元素的数列
        # distList = [dict() for i in range(N)]

        # for i in xrange(1, N):
        #     for j in range(i):
        #         delta = A[i] - A[j]

        #         # 考虑只包含 A[j], A[i]的数列
        #         if delta in distList[i]:
        #             distList[i][delta] += 1
        #         else:
        #             distList[i][delta] = 1
        #         if delta in distList[j]:
        #             # A[i] 可以加到所有以A[j]结尾的公差为delta的数列后面
        #             distList[i][delta] += distList[j][delta]
        #             num += distList[j][delta]
        # return num

        # 1. 动态规划 + 哈希表
        # 我们首先考虑至少有两个元素的等差子序列，下文将其称作弱等差子序列。
        # 由于题目要统计的等差子序列至少有三个元素，我们回顾上述二重循环，其中「将 nums[i] 加到以 nums[j] 为尾项，公差为 d 的弱等差子序列的末尾」这一操作，实际上就构成了一个至少有三个元素的等差子序列，因此我们将循环中的 f[j][d] 累加，即为答案。
        # 代码实现时，由于 nums[i] 的范围很大，所以计算出的公差的范围也很大，我们可以将状态转移数组 f 的第二维用哈希表代替。
        ans = 0
        # 由于尾项和公差可以确定一个等差数列，因此我们定义状态 f[i][d] 表示尾项为 nums[i]，公差为 d 的弱等差子序列的个数。
        f = [collections.defaultdict(int) for _ in nums]
        # 我们用一个二重循环去遍历 nums 中的所有元素对(nums[i], nums[j])，其中 j < i。将 nums[i] 和 nums[j] 分别当作等差数列的尾项和倒数第二项，则该等差数列的公差 d = nums[i]−nums[j]。由于公差相同，我们可以将 nums[i] 加到以 nums[j] 为尾项，公差为 d 的弱等差子序列的末尾，这对应着状态转移 f[i][d] += f[j][d]。同时，(nums[i], nums[j]) 这一对元素也可以当作一个弱等差子序列，故有状态转移  f[i][d] += f[j][d]+1
        for i, x in enumerate(nums):
            for j in range(i):
                d = x - nums[j]
                cnt = f[j][d]
                ans += cnt
                f[i][d] += cnt + 1
        return ans
        # 复杂度分析
        # 时间复杂度：O(n ^ 2)，其中 n 是数组 nums 的长度。
        # 空间复杂度：O(n ^ 2)。
        # 执行用时：636 ms, 在所有 Python 提交中击败了69.57 % 的用户
        # 内存消耗：72.3 MB, 在所有 Python 提交中击败了30.44 % 的用户


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([2, 4, 6, 8, 10], 7),
        ([7, 7, 7, 7, 7], 16),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.numberOfArithmeticSlices(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)

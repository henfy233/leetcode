# -*- encoding: utf-8 -*-
'''
@File    :   1713.得到子序列的最少操作次数.py
@Time    :   2021/07/26 02:16:27
@Author  :   henfy
@Diffi   :   Hard
@Version :   1.0

题目：https://leetcode-cn.com/problems/minimum-operations-to-make-a-subsequence/
'''
import bisect
from typing import List


class Solution(object):
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        # 1. 贪心 + 二分查找
        # https://leetcode-cn.com/problems/minimum-operations-to-make-a-subsequence/solution/de-dao-zi-xu-lie-de-zui-shao-cao-zuo-ci-hefgl/
        pos = dict()
        n = len(target)
        for i in range(n):
            pos[target[i]] = i
        d = []
        for val in arr:
            if val in pos:
                idx = pos[val]
                it = bisect.bisect_left(d, idx)
                if it < len(d):
                    d[it] = idx
                else:
                    d.append(idx)
        return n - len(d)
        # 复杂度分析
        # 时间复杂度：O(n+mlogm)，其中 n 是数组 target 的长度，m 是数组 arr 的长度。遍历 target 需要 O(n) 的时间，求 arr′的最长递增子序列需要 O(mlogm) 的时间。
        # 空间复杂度：O(n+m)。需要 O(n) 大小的哈希表存储 target 的元素的下标，以及 O(m) 的空间求最长递增子序列。

        # 简洁写法
        # pos = {val: i for i, val in enumerate(target)}
        # dp = list()
        # for num in arr:
        #     if num in pos:
        #         idx = pos[num]
        #         if not dp or dp[-1] < idx:
        #             dp.append(idx)
        #         else:
        #             dp[bisect.bisect_left(dp, idx)] = idx
        # return len(target) - len(dp)


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([5, 1, 3], [9, 4, 2, 3, 4], 2),
        ([6, 4, 8, 1, 3, 2], [4, 7, 6, 2, 3, 8, 6, 1], 3),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.minOperations(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)

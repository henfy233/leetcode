#
# @lc app=leetcode.cn id=1713 lang=python
#
# [1713] 得到子序列的最少操作次数
#
import bisect
# @lc code=start


class Solution(object):
    def minOperations(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: int
        """
        # 贪心 + 二分查找
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
# @lc code=end


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

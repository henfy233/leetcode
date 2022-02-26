# -*- encoding: utf-8 -*-
'''
@File    :   5859. 差的绝对值为 K 的数对数目.py
@Time    :   2021/09/18 22:35:42
@Author  :   henfy
@Diffi   :   Easy
@Version :   1.0

题目：https://leetcode-cn.com/contest/biweekly-contest-61/problems/count-number-of-pairs-with-absolute-difference-k/
'''


from typing import List


class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        # 自己做，暴力
        n = len(nums)
        ans = 0
        for i in range(n-1):
            for j in range(i+1, n):
                if abs(nums[i] - nums[j]) == k:
                    ans += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([1, 2, 2, 1], 1, 4),
        ([1, 3], 3, 0),
        ([3, 2, 1, 5, 4], 2, 3),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.countKDifference(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)

# -*- encoding: utf-8 -*-
'''
@File    :   2044. 统计按位或能得到最大值的子集数目.py
@Time    :   2022/03/15 00:21:11
@Author  :   henfy
@Diffi   :   Middle
@Version :   1.0

题目：https://leetcode-cn.com/problems/count-number-of-maximum-bitwise-or-subsets/
'''


from functools import reduce
from operator import or_
from typing import List


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        # nums = sorted(nums, reverse=True)
        # print(nums)
        # x,n = nums[0], len(nums)
        # size = 1
        # for i in range(1, n):
        #     if x == nums[i]:
        #         size+=1
        #     else:
        #         break

        # 位运算
        # maxOr, cnt = 0, 0
        # for i in range(1, 1 << len(nums)):
        #     orVal = reduce(
        #         or_, (num for j, num in enumerate(nums) if (i >> j) & 1), 0)
        #     if orVal > maxOr:
        #         maxOr, cnt = orVal, 1
        #     elif orVal == maxOr:
        #         cnt += 1
        # return cnt

        # 回溯
        maxOr, cnt = 0, 0

        def dfs(pos: int, orVal: int) -> None:
            if pos == len(nums):
                nonlocal maxOr, cnt
                if orVal > maxOr:
                    maxOr, cnt = orVal, 1
                elif orVal == maxOr:
                    cnt += 1
                return
            dfs(pos + 1, orVal | nums[pos])
            dfs(pos + 1, orVal)
        dfs(0, 0)
        return cnt


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([3, 1], 2),
        ([2, 2, 2], 7),
        ([3, 2, 1, 5], 6)
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.countMaxOrSubsets(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)

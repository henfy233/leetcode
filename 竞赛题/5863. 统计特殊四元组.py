# -*- encoding: utf-8 -*-
'''
@File    :   5863. 统计特殊四元组.py
@Time    :   2021/09/05 10:31:27
@Author  :   henfy
@Diffi   :   Easy
@Version :   1.0

题目：https://leetcode-cn.com/contest/weekly-contest-257/problems/count-special-quadruplets/
'''


from typing import List


class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        n = len(nums)
        num = 0
        for x in range(n-3):
            for y in range(x+1, n-2):
                for z in range(y+1, n-1):
                    for i in range(z+1, n):
                        sum = nums[x]+nums[y]+nums[z]
                        if sum == nums[i]:
                            num += 1
        return num


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([1, 2, 3, 6], 1),
        ([3, 3, 6, 4, 5], 0),
        ([1, 1, 1, 3, 5], 4),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.countQuadruplets(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)

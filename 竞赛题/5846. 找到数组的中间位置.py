# -*- encoding: utf-8 -*-
'''
@File    :   5846. 找到数组的中间位置.py
@Time    :   2021/09/04 22:33:02
@Author  :   henfy
@Diffi   :   Easy
@Version :   1.0

题目：https://leetcode-cn.com/contest/biweekly-contest-60/problems/find-the-middle-index-in-array/
'''


from typing import List


class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            sum1 = sum(nums[:i])
            sum2 = sum(nums[i+1:])
            # print('sum1', sum1, 'sum2', sum2)
            if sum1 == sum2:
                return i
        return -1


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([2, 3, -1, 8, 4], 3),
        ([1, -1, 4], 2),
        ([2, 5], -1),
        ([1], 0),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.findMiddleIndex(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)

# -*- encoding: utf-8 -*-
'''
@File    :   553. 最优除法.py
@Time    :   2022/02/27 15:53:58
@Author  :   henfy
@Diffi   :   Middle
@Version :   1.0

题目：https://leetcode-cn.com/problems/optimal-division/
'''


from typing import List


class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        # 不会做

        # 数学
        if len(nums) == 1:
            return str(nums[0])
        if len(nums) == 2:
            return str(nums[0]) + "/" + str(nums[1])
        return str(nums[0]) + "/(" + "/".join(map(str, nums[1:])) + ")"


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([1000, 100, 10, 2], "1000/(100/10/2)"),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.optimalDivision(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)

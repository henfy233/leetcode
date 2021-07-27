#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   只出现一次的数字.py
@Time    :   2021/07/24 11:18:54
@Author  :   henfy
@Version :   1.0
'''

# here put the import lib


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 字典dict解决
        # d = dict()
        # for i in range(len(nums)):
        #     if d.get(nums[i]):
        #         del d[nums[i]]
        #     else:
        #         d[nums[i]] = i+1
        # print(d)
        # return d.keys()[0]

        # 位运算解决
        result = 0
        for i in range(len(nums)):
            result ^= nums[i]
        return result


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([2, 2, 1], 1),
        ([4, 1, 2, 1, 2], 4)
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.singleNumber(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)

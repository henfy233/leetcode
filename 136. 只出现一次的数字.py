'''
@File    :   136. 只出现一次的数字.py
@Time    :   2021/09/01 01:13:42
@Author  :   henfy
@Diffi   :   Easy
@Version :   1.0

题目：https://leetcode-cn.com/problems/single-number/
'''


from typing import List
from functools import reduce


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 自己写，字典dict解决，内存问题，对位运算还是模糊
        d = dict()
        for i in range(len(nums)):
            if d.get(nums[i]):
                del d[nums[i]]
            else:
                d[nums[i]] = i+1
        for key in d.keys():
            return key

        # 1.1 位运算解决
        # result = 0
        # for i in range(len(nums)):
        #     result ^= nums[i]
        # return result

        # 1.2 位运算解决
        # return reduce(lambda x, y: x ^ y, nums)


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

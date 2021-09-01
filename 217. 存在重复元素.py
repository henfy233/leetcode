# -*- encoding: utf-8 -*-
'''
@File    :   217. 存在重复元素.py
@Time    :   2021/07/24 11:19:45
@Author  :   henfy
@Diffi   :   Easy
@Version :   1.0

题目：https://leetcode-cn.com/problems/contains-duplicate/
'''


from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # 哈希表
        # d = dict()
        # for i in range(len(nums)):
        #     # print(i, nums[i])
        #     # print('d.get(nums[i])',d.get(nums[i]))
        #     if d.get(nums[i]):
        #         return True
        #     d[nums[i]] = i+1
        # # print(d)
        # return False

        # 排序
        # nums = sorted(nums)
        # for i in range(1,len(nums)):
        #     if nums[i] == nums[i-1]:
        #         return True
        # return False

        # 长度
        if len(nums) != len(set(nums)):
            return True
        return False


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([1, 2, 3, 1], True),
        ([1, 2, 3, 4], False),
        ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True)
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.containsDuplicate(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)

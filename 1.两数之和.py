# -*- encoding: utf-8 -*-
'''
@File    :   1.两数之和.py
@Time    :   2021/07/27 22:31:43
@Author  :   henfy
@Diffi   :   Easy
@Version :   1.0

题目：https://leetcode-cn.com/problems/two-sum/
'''


from typing import List


class Solution(object):
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # print(nums)
        d = dict()
        n = len(nums)
        for i in range(n):
            if target - nums[i] in d:
                return [d[target - nums[i]], i]
            d[nums[i]] = i

        # 1.1 暴力破解
        # https://leetcode-cn.com/problems/two-sum/solution/liang-shu-zhi-he-by-leetcode-solution/
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        # 1.2 暴力破解
        # n = len(nums)
        # for i in range(n):
        #     if target - nums[i] in nums:
        #         j = nums.index(target - nums[i])
        #         if(j != i):
        #             break
        # if(j > i):
        #     return [i, j]
        # else:
        #     return [j, i]

        # 2.哈希表 数组存储索引
        # hashmap = dict()
        # # hashmap = {}
        # for i, num in enumerate(nums):
        #     if target - num in hashmap:
        #         return [hashmap[target-num], i]
        #     hashmap[num] = i


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.twoSum(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)

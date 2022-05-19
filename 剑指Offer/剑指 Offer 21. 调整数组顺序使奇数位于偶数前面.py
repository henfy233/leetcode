# -*- encoding: utf-8 -*-
'''
@File    :   剑指 Offer 21. 调整数组顺序使奇数位于偶数前面.py
@Time    :   2022/05/15 00:16:29
@Author  :   henfy
@Diffi   :   Easy
@Method  :   双指针

题目：https://leetcode.cn/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof/
'''


from typing import List


class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        # 自己想
        # arr1, arr2 = [], []
        # for x in nums:
        #     # print(x)
        #     if x % 2 != 0:
        #         arr1.append(x)
        #     else:
        #         arr2.append(x)
        # return arr1+arr2

        # 双指针
        i, j = 0, len(nums) - 1
        while i < j:
            while i < j and nums[i] & 1 == 1:
                i += 1
            while i < j and nums[j] & 1 == 0:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        return nums


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([1, 2, 3, 4], [1, 3, 2, 4]),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.exchange(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)

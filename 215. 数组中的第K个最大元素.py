# -*- encoding: utf-8 -*-
'''
@File    :   215. 数组中的第K个最大元素.py
@Time    :   2022/09/10 18:52:25
@Author  :   henfy
@Diffi   :   Easy
@Method  :   优先队列、快排、分治
@Question:   https://leetcode.cn/problems/kth-largest-element-in-an-array/
@Answer  :
'''

from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 暴力解法，冒泡排序，返回下标 k-1 自己写的
        for i in range(len(nums)):
            for j in range(len(nums)-i-k):
                if nums[j+1] > nums[j]:
                    nums[j+1], nums[j] = nums[j], nums[j+1]
        print(nums)
        return nums[-k]


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([3, 2, 1, 5, 6, 4], 2, 5),
        ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.findKthLargest(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)

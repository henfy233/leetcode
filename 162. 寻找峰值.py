# -*- encoding: utf-8 -*-
'''
@File    :   162. 寻找峰值.py
@Time    :   2021/09/15 10:09:51
@Author  :   henfy
@Diffi   :   Medium
@Version :   1.0

题目：https://leetcode-cn.com/problems/find-peak-element/
'''


from typing import List
import random


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # 自己写，总感觉有点不对劲
        n = len(nums)
        if n == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        elif nums[n-1] > nums[n-2]:
            return n-1
        for i in range(1, n-1):
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                return i
        # 执行用时：36 ms, 在所有 Python3 提交中击败了44.22 % 的用户
        # 内存消耗：14.9 MB, 在所有 Python3 提交中击败了87.49 % 的用户

        # 1. 寻找最大值
        # https://leetcode-cn.com/problems/find-peak-element/solution/xun-zhao-feng-zhi-by-leetcode-solution-96sj/
        # idx = 0
        # for i in range(1, len(nums)):
        #     if nums[i] > nums[idx]:
        #         idx = i
        # return idx
        # 时间复杂度：O(n)，其中 n 是数组 nums 的长度。
        # 空间复杂度：O(1)。

        # 2. 迭代爬坡
        # https://leetcode-cn.com/problems/find-peak-element/solution/xun-zhao-feng-zhi-by-leetcode-solution-96sj/
        # n = len(nums)
        # idx = random.randint(0, n - 1)
        # # 辅助函数，输入下标 i，返回 nums[i] 的值
        # # 方便处理 nums[-1] 以及 nums[n] 的边界情况
        # def get(i: int) -> int:
        #     if i == -1 or i == n:
        #         return float('-inf')
        #     return nums[i]

        # while not (get(idx - 1) < get(idx) > get(idx + 1)):
        #     if get(idx) < get(idx + 1):
        #         idx += 1
        #     else:
        #         idx -= 1

        # return idx
        # 时间复杂度：O(n)，其中 n 是数组 nums 的长度。在最坏情况下，数组 nums 单调递增，并且我们随机到位置 0，这样就需要向右走到数组 nums 的最后一个位置。
        # 空间复杂度：O(1)。

        # 3. 方法二的二分查找优化
        # https://leetcode-cn.com/problems/find-peak-element/solution/xun-zhao-feng-zhi-by-leetcode-solution-96sj/
        # n = len(nums)
        # # 辅助函数，输入下标 i，返回 nums[i] 的值
        # # 方便处理 nums[-1] 以及 nums[n] 的边界情况
        # def get(i: int) -> int:
        #     if i == -1 or i == n:
        #         return float('-inf')
        #     return nums[i]

        # left, right, ans = 0, n - 1, -1
        # while left <= right:
        #     mid = (left + right) // 2
        #     if get(mid - 1) < get(mid) > get(mid + 1):
        #         ans = mid
        #         break
        #     if get(mid) < get(mid + 1):
        #         left = mid + 1
        #     else:
        #         right = mid - 1
        # return ans


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([1, 2, 3, 1], 2),
        ([1, 2, 1, 3, 5, 6, 4], 1 or 5),
        ([1], 0),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.findPeakElement(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)

# -*- encoding: utf-8 -*-
'''
@File    :   704. 二分查找.py
@Time    :   2021/09/06 00:37:07
@Author  :   henfy
@Diffi   :   Easy
@Version :   1.0

题目：https://leetcode-cn.com/problems/binary-search/
'''


from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 自己做，之前做过有印象
        # def bisect(left, right):
        #     if left > right:
        #         return -1
        #     mid = (left+right)//2
        #     print(mid)
        #     if nums[mid] == target:
        #         return mid
        #     elif nums[mid] > target:
        #         return bisect(left, mid-1)
        #     else:
        #         return bisect(mid+1, right)

        # return bisect(0, len(nums)-1)
        # 执行用时：36 ms, 在所有 Python3 提交中击败了83.39 % 的用户
        # 内存消耗：22.6 MB, 在所有 Python3 提交中击败了5.29 % 的用户

        # 1. 二分查找
        # https://leetcode-cn.com/problems/binary-search/solution/er-fen-cha-zhao-by-leetcode-solution-f0xw/
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (high - low) // 2 + low
            num = nums[mid]
            if num == target:
                return mid
            elif num > target:
                high = mid - 1
            else:
                low = mid + 1
        return -1
        # 时间复杂度：O(logn)，其中 nn 是数组的长度。
        # 空间复杂度：O(1)。
        # 执行用时：32 ms, 在所有 Python3 提交中击败了94.66 % 的用户
        # 内存消耗：15.6 MB, 在所有 Python3 提交中击败了99.32 % 的用户


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([-1, 0, 3, 5, 9, 12], 9, 4),
        ([-1, 0, 3, 5, 9, 12], 2, -1),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.search(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)

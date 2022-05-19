# -*- encoding: utf-8 -*-
'''
@File    :   剑指 Offer 53 - I. 在排序数组中查找数字 I.py
@Time    :   2022/04/25 01:44:12
@Author  :   henfy
@Diffi   :   Easy
@Version :   1.0

题目：https://leetcode-cn.com/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof/
'''

import bisect
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 以前作弊法
        # n = len(nums)
        # sum = 0
        # index = bisect.bisect_left(nums, target)
        # for i in range(index, n):
        #     if nums[i] != target:
        #         break
        #     sum = sum+1
        # return sum

        # 代码写错啦
        # n = len(nums)
        # left, right = 0, 1
        # mid = n//2
        # # print(mid)
        # if mid == 0:
        #     return
        # if target > nums[mid]:
        #     self.search(nums[mid:], target)
        # elif target < nums[mid]:
        #     self.search(nums[:mid], target)
        # else:
        #     left = mid
        #     right = mid
        #     while left >= 0:
        #         if nums[left] != target:
        #             break
        #         left -= 1
        #     while right < n:
        #         if nums[right] != target:
        #             break
        #         right += 1
        # return right-left-1

        # 二分法
        # # 搜索右边界 right
        # i, j = 0, len(nums)-1
        # while i <= j:
        #     mid = (i+j)//2
        #     if nums[mid] <= target:
        #         i = mid + 1
        #     else:
        #         j = mid-1
        # right = i

        # # 若数组中无 target ，则提前返回
        # if j >= 0 and nums[j] != target:
        #     return 0

        # # 搜索左边界 left
        # i = 0
        # while i <= j:
        #     mid = (i+j)//2
        #     if nums[mid] < target:
        #         i = mid+1
        #     else:
        #         j = mid - 1
        # left = j
        # return right-left-1

        # 解法优化
        def helper(tar):
            i, j = 0, len(nums) - 1
            while i <= j:
                m = (i + j) // 2
                if nums[m] <= tar:
                    i = m + 1
                else:
                    j = m - 1
            return i
        return helper(target) - helper(target - 1)
        '''
        作者：jyd
        链接：https://leetcode-cn.com/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof/solution/mian-shi-ti-53-i-zai-pai-xu-shu-zu-zhong-cha-zha-5/
        来源：力扣（LeetCode）
        著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        '''


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([5, 7, 7, 8, 8, 10], 8, 2),
        ([5, 7, 7, 8, 8, 10], 6, 0),
        ([1], 1, 1),
        ([], 0, 0),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.search(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)

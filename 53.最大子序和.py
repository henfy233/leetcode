# -*- encoding: utf-8 -*-
'''
@File    :   53.最大子序和.py
@Time    :   2021/08/29 23:48:18
@Author  :   henfy
@Diffi   :   Middle
@Method  :   动态规划、分治法
@Question:   https://leetcode-cn.com/problems/maximum-subarray/
@Answer1 :   https://leetcode.cn/problems/maximum-subarray/solutions/9058/dong-tai-gui-hua-fen-zhi-fa-python-dai-ma-java-dai/
@Answer2 :   https://leetcode.cn/problems/maximum-subarray/solutions/228009/zui-da-zi-xu-he-by-leetcode-solution/
'''

from typing import List
# NOTE 继续练习

class Solution(object):
    def maxSubArray(self, nums: List[int]) -> int:
        # 自己想，动态规划，这种不好
        sum = 0
        for i in range(len(nums)):
            # sum += nums[i]
            nums[i] = max(sum + nums[i], nums[i])
            sum = nums[i]
        return max(nums)

        # 当前值 之前和    当前和 最大和 自己写
        #     num  beforeAll nowAll sum
        # beforeAll = 0
        # nowAll = 0
        # flag = None
        # for num in nums:
        #     nowAll = max(num, beforeAll+num)
        #     if not flag:
        #         sum = max(num, nowAll)
        #     else:
        #         sum = max(num, nowAll, beforeAll)
        #     # print("sum=%d", sum)
        #     if sum > flag:
        #         flag = sum
        #     beforeAll = nowAll
        # return flag

        # 动态规划 滚动数组
        # pre = 0
        # maxAns = nums[0]
        # for num in nums:
        #     pre = max(num, pre+num)
        #     maxAns = max(maxAns, pre)
        # return maxAns

        # 2.1
        # n = len(nums)
        # for i in range(1, n):
        #     # nums[i] = max(nums[i-1]+nums[i], nums[i])
        #     if nums[i-1] > 0:
        #         nums[i] += nums[i-1]
        # return max(nums)

# 分治法
# class Solution(object):
#     def maxSubArray(self, nums: List[int]) -> int:
#       n = len(nums)
#       if n==0:
#         return 0
#       return self.__max_sub_array(nums, 0, n-1)

#     def __max_sub_array(self, nums, left, right):
#       if left == right:
#         return nums[left]
#       mid = (left+right)>>1
#       return max(self.__max_sub_array(nums, left, mid),
#                 self.__max_sub_array(nums, mid+1, right),
#                 self.__max_cross_array(nums, left, mid, right))

#     def __max_cross_array(self, nums, left, mid, right):
#       # 一定包含 nums[mid] 元素的最大连续子数组的和，
#       # 思路是看看左边"扩散到底"，得到一个最大数，右边"扩散到底"得到一个最大数
#       # 然后再加上中间数
#       left_sum_max = 0
#       start_left = mid - 1
#       s1 = 0
#       while start_left >= left:
#           s1 += nums[start_left]
#           left_sum_max = max(left_sum_max, s1)
#           start_left -= 1

#       right_sum_max = 0
#       start_right = mid + 1
#       s2 = 0
#       while start_right <= right:
#           s2 += nums[start_right]
#           right_sum_max = max(right_sum_max, s2)
#           start_right += 1
#       return left_sum_max + nums[mid] + right_sum_max

if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
        ([1], 1),
        ([0], 0),
        ([-1], -1),
        ([-100000], -100000),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.maxSubArray(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)

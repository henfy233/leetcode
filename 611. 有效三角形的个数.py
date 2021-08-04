#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   611. 有效三角形的个数.py
@Time    :   2021/08/04 00:23:48
@Author  :   henfy
@Version :   1.0
'''

# here put the import lib


class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 暴力 自己写，思路正确，但超时了
        # count = 0
        # nums.sort()
        # n = len(nums)
        # for x in range(n-2):
        #     for y in range(x+1, n-1):
        #         for z in range(y+1, n):
        #             if nums[x] + nums[y] > nums[z]:
        #                 count += 1
        # return count

        # 排序 + 二分查找 也超时了
        # import bisect
        # count = 0
        # nums.sort()
        # n = len(nums)
        # for x in range(n):
        #     for y in range(x+1, n):
        #         right = bisect.bisect_left(nums, nums[x] + nums[y])
        #         print('right', right)
        #         left = y+1
        #         print('left', left)
        #         if left >= right:
        #             continue
        #         count += right - left
        # return count

        # 1. 排序 + 二分查找 勉强能通过，但是速度还是很慢
        # count = 0
        # nums.sort()
        # n = len(nums)
        # # 二重循环枚举 x 和 y
        # for x in range(n):
        #     for y in range(x+1, n):
        #         # 我们可以在 [j+1,n-1] [j+1,n−1] 的下标范围内使用二分查找（其中 n 是数组 nums 的长度）
        #         # 找出最大的满足 nums[k] < nums[i] + nums[j]nums[k] < nums[i]+nums[j] 的下标 k
        #         left, right, k = y+1, n-1, y
        #         while left <= right:
        #             mid = (left+right)//2
        #             if nums[mid] < nums[x]+nums[y]:
        #                 # 若二分查找失败，我们可以令 k = y，此时对应的范围长度 k - y = 0，我们也就保证了答案的正确性。
        #                 k = mid
        #                 left = mid+1
        #             else:
        #                 right = mid-1
        #         count += k - y
        # return count
        # 执行用时：5724 ms, 在所有 Python 提交中击败了5.71 % 的用户
        # 内存消耗：13.2 MB, 在所有 Python 提交中击败了21.43 % 的用户

        # 2. 排序 + 双指针
        # 如果我们固定 i，那么随着 j的递增，不等式右侧 nums[i]+nums[j] 也是递增的，因此k_i,j也是递增的。
        # n = len(nums)
        # nums.sort()
        # ans = 0
        # # 我们使用一重循环枚举 i
        # for i in range(n):
        #     k = i
        #     # 当 i 固定时，我们使用双指针同时维护 j 和 k，它们的初始值均为 i。
        #     # 我们每一次将 j向右移动一个位置，即 j←j+1，并尝试不断向右移动 k，
        #     # 使得 k是最大的满足 nums[k] < nums[i]+nums[j] 的下标。
        #     for j in range(i + 1, n):
        #         # print('i', i)
        #         # print('j', j)
        #         # print('k', k)
        #         while k + 1 < n and nums[k + 1] < nums[i] + nums[j]:
        #             k += 1
        #         ans += max(k - j, 0)
        # return ans

        # 3. 一次遍历 排序 + 双指针
        nums.sort()
        n = len(nums)
        ans = 0
        # k为最后一个索引
        for k in range(2, n):
            i, j = 0, k-1
            while i < j:
                # 如果k前面的 i j 相加大于 k，则相加相差值。
                if nums[i] + nums[j] > nums[k]:
                    ans += j-i
                    j -= 1
                # 否则 i++
                else:
                    i += 1
        return ans
        # 执行用时：508 ms, 在所有 Python 提交中击败了94.29%的用户
        # 内存消耗：13.3 MB, 在所有 Python 提交中击败了10.00%的用户


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([2, 2, 3, 4], 3),
        ([2, 2, 4, 5], 2),
        ([0, 0, 0], 0),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.triangleNumber(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)

# -*- encoding: utf-8 -*-
'''
@File    :   1109. 航班预订统计.py
@Time    :   2021/08/31 00:03:02
@Author  :   henfy
@Diffi   :   Easy
@Version :   1.0

题目：https://leetcode-cn.com/problems/corporate-flight-bookings/
'''


from typing import List


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        # 自己做，超出时间限制，就是不会做
        # arr = [0]*(n+1)
        # for i in range(len(bookings)):
        #     for j in range(bookings[i][0], bookings[i][1]+1):
        #         arr[j] += bookings[i][2]
        # return arr[1:]

        # 1. 差分
        # https://leetcode-cn.com/problems/corporate-flight-bookings/solution/hang-ban-yu-ding-tong-ji-by-leetcode-sol-5pv8/
        nums = [0] * n
        for left, right, inc in bookings:
            nums[left - 1] += inc
            if right < n:
                nums[right] -= inc
        for i in range(1, n):
            nums[i] += nums[i - 1]
        return nums
        # 时间复杂度：O(n+m)，其中 n 为要求的数组长度，m 为预定记录的数量。我们需要对于每一条预定记录处理一次差分数组，并最后对差分数组求前缀和。
        # 空间复杂度：O(1)。我们只需要常数的空间保存若干变量，注意返回值不计入空间复杂度。


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([[1, 2, 10], [2, 3, 20], [2, 5, 25]], 5, [10, 55, 45, 25, 25]),
        ([[1, 2, 10], [2, 2, 15]], 2, [10, 25]),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.corpFlightBookings(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)

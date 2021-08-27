# -*- encoding: utf-8 -*-
'''
@File    :   1818.绝对差值和.py
@Time    :   2021/07/14 02:28:47
@Author  :   henfy
@Diffi   :   Medium
@Version :   1.0

题目：https://leetcode-cn.com/problems/minimum-absolute-sum-difference/
'''
import bisect
from typing import List


class Solution(object):
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        # 1. 排序 + 二分查找
        # https://leetcode-cn.com/problems/minimum-absolute-sum-difference/solution/jue-dui-chai-zhi-he-by-leetcode-solution-gv78/
        n = len(nums1)
        total = 0
        ans = float("inf")
        sl = sorted(nums1)
        for i in range(n):
            diff = abs(nums1[i] - nums2[i])
            total += diff
            idx = bisect.bisect_left(sl, nums2[i])
            # idx > 0 尝试用idx-1替换当前值
            if idx:
                ans = min(ans, abs(sl[idx-1] - nums2[i]) - diff)
            # idx < n 尝试用idx替换当前值
            if idx < n:
                ans = min(ans, abs(sl[idx] - nums2[i]) - diff)
        return (total + ans) % (10 ** 9 + 7) if total else total
        # 复杂度分析
        # 时间复杂度：O(nlogn)，其中 n 是数组 nums_1和 nums_2的长度。我们需要记录 nums_1​中的元素，并进行排序，时间复杂度是 O(nlogn)。计算 maxn 需要进行 n 次二分查找，每次二分查找的时间为 O(logn)，因此时间复杂度也是 O(nlogn)。所以总的时间复杂度为 O(nlogn)。
        # 空间复杂度：O(n)，其中 n 是数组 nums_1和 nums_2的长度。我们需要创建大小为 n 的辅助数组。

        # sum = 0
        # list = []
        # list1 = []
        # print('nums1',len(nums1))
        # print('nums2',len(nums2))
        # for i in range(len(nums1)):
        #     diff = abs(nums1[i]-nums2[i])
        #     list.append(diff)
        #     sum += diff
        # print('list1',list)
        # print(max(list))
        # index = list.index(max(list))
        # print('index',index)
        # sum -= max(list)
        # for i in range(len(nums1)):
        #     diff = abs(nums1[i]-nums2[index])
        #     list1.append(diff)
        # print('list2',list1)
        # # index = list.index(min(list))
        # # print(index)
        # # print(nums1[index])
        # # diff = abs(nums1[index]-nums2[index])
        # sum += min(list1)
        # return sum


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([1, 7, 5], [2, 3, 5], 3),
        ([2, 4, 6, 8, 10], [2, 4, 6, 8, 10], 0),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.minAbsoluteSumDiff(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)

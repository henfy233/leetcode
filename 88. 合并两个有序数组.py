# -*- encoding: utf-8 -*-
'''
@File    :   88. 合并两个有序数组.py
@Time    :   2021/08/31 10:44:18
@Author  :   henfy
@Diffi   :   Easy
@Version :   1.0

题目：https://leetcode-cn.com/problems/merge-sorted-array/
'''


from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # 自己做，双指针，通过了，就是最后一段代码不会
        # i, j = 0, 0
        # arr = []
        # while i != m and j != n:
        #     if nums1[i] < nums2[j]:
        #         arr.append(nums1[i])
        #         i += 1
        #     else:
        #         arr.append(nums2[j])
        #         j += 1
        # if i != m:
        #     arr.extend(nums1[i:m])
        # else:
        #     arr.extend(nums2[j:n])
        # print(arr)
        # nums1[:] = arr
        # return nums1

        # 1. 合并后排序
        # https://leetcode-cn.com/problems/merge-sorted-array/solution/he-bing-liang-ge-you-xu-shu-zu-by-leetco-rrb0/
        # nums1[m:] = nums2
        # nums1.sort()
        # 时间复杂度：O((m+n)log(m+n))。
        # 排序序列长度为 m+n，套用快速排序的时间复杂度即可，平均情况为 O((m+n)log(m+n))。
        # 空间复杂度：O(log(m+n))。
        # 排序序列长度为 m+n，套用快速排序的空间复杂度即可，平均情况为 O(log(m+n))。

        # 2. 双指针
        # https://leetcode-cn.com/problems/merge-sorted-array/solution/he-bing-liang-ge-you-xu-shu-zu-by-leetco-rrb0/
        # sorted = []
        # p1, p2 = 0, 0
        # while p1 < m or p2 < n:
        #     if p1 == m:
        #         sorted.append(nums2[p2])
        #         p2 += 1
        #     elif p2 == n:
        #         sorted.append(nums1[p1])
        #         p1 += 1
        #     elif nums1[p1] < nums2[p2]:
        #         sorted.append(nums1[p1])
        #         p1 += 1
        #     else:
        #         sorted.append(nums2[p2])
        #         p2 += 1
        # nums1[:] = sorted
        # return nums1
        # 时间复杂度：O(m+n)。
        # 指针移动单调递增，最多移动 m+n 次，因此时间复杂度为 O(m+n)。
        # 空间复杂度：O(m+n)。
        # 需要建立长度为 m+n 的中间数组 sorted。

        # 3. 逆向双指针
        p1, p2 = m - 1, n - 1
        tail = m + n - 1
        while p1 >= 0 or p2 >= 0:
            if p1 == -1:
                nums1[tail] = nums2[p2]
                p2 -= 1
            elif p2 == -1:
                nums1[tail] = nums1[p1]
                p1 -= 1
            elif nums1[p1] > nums2[p2]:
                nums1[tail] = nums1[p1]
                p1 -= 1
            else:
                nums1[tail] = nums2[p2]
                p2 -= 1
            tail -= 1
        return nums1
        # 时间复杂度：O(m+n)。
        # 指针移动单调递减，最多移动 m+n 次，因此时间复杂度为 O(m+n)。
        # 空间复杂度：O(1)。
        # 直接对数组 nums_1原地修改，不需要额外空间。


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
        ([1], 1, [], 0, [1]),
        ([0], 0, [1], 1, [1]),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.merge(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)

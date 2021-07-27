#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   两个数组的交集 II.py
@Time    :   2021/07/24 11:28:01
@Author  :   henfy
@Version :   1.0
'''

# here put the import lib


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # 数组进行排序
        # nums1.sort()
        # nums2.sort()
        # # print(nums1, nums2)
        # l = []
        # left = 0
        # right = 0
        # while left < len(nums1) and right < len(nums2):
        #     if nums1[left] < nums2[right]:
        #         left += 1
        #     elif nums1[left] > nums2[right]:
        #         right += 1
        #     else:
        #         l.append(nums1[left])
        #         left += 1
        #         right += 1
        # # print(l)
        # return l

        # 使用map解决
        d = dict()
        l = []
        for i in range(len(nums1)):
            if nums1[i] in d:
                d[nums1[i]] += 1
            else:
                d[nums1[i]] = 1
        for i in range(len(nums2)):
            if nums2[i] in d:
                if d[nums2[i]] >= 1:
                    # print(d.get(nums2[i]))
                    l.append(nums2[i])
                    d[nums2[i]] -= 1
        l.sort()
        return l


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([1, 2, 2, 1], [2, 2], [2, 2]),
        ([4, 9, 5], [9, 4, 9, 8, 4], [4, 9]),
        ([4, 9, 5], [9, 4, 5, 5, 4], [4, 5, 9])
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        print(test)
        test_result = s.intersect(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)

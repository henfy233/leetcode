# -*- encoding: utf-8 -*-
'''
@File    :   剑指 Offer 40. 最小的k个数.py
@Time    :   2022/05/24 17:24:23
@Author  :   henfy
@Diffi   :   Easy
@Method  :   排序（中等）

题目：https://leetcode.cn/problems/zui-xiao-de-kge-shu-lcof/
'''


from typing import List


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        # arr.sort()
        # # print(arr)
        # return arr[:k]

        # 快速排序
        # def quick_sort(arr, l, r):
        #     # 子数组长度为 1 时终止递归
        #     if l >= r:
        #         return
        #     # 哨兵划分操作（以 arr[l] 作为基准数）
        #     i, j = l, r
        #     while i < j:
        #         while i < j and arr[j] >= arr[l]:
        #             j -= 1
        #         while i < j and arr[i] <= arr[l]:
        #             i += 1
        #         arr[i], arr[j] = arr[j], arr[i]
        #     arr[l], arr[i] = arr[i], arr[l]
        #     # 递归左（右）子数组执行哨兵划分
        #     quick_sort(arr, l, i - 1)
        #     quick_sort(arr, i + 1, r)

        # quick_sort(arr, 0, len(arr) - 1)
        # return arr[:k]

        # 基于快速排序的数组划分
        if k >= len(arr):
            return arr

        def quick_sort(l, r):
            i, j = l, r
            while i < j:
                while i < j and arr[j] >= arr[l]:
                    j -= 1
                while i < j and arr[i] <= arr[l]:
                    i += 1
                arr[i], arr[j] = arr[j], arr[i]
            arr[l], arr[i] = arr[i], arr[l]
            if k < i:
                return quick_sort(l, i - 1)
            if k > i:
                return quick_sort(i + 1, r)
            return arr[:k]

        return quick_sort(0, len(arr) - 1)


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([3, 2, 1], 2, [1, 2]),
        ([0, 1, 2, 1], 1, [0]),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.getLeastNumbers(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)

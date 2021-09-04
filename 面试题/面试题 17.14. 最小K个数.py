# -*- encoding: utf-8 -*-
'''
@File    :   面试题 17.14. 最小K个数.py
@Time    :   2021/09/03 00:13:11
@Author  :   henfy
@Diffi   :   Medium
@Version :   1.0

题目：https://leetcode-cn.com/problems/smallest-k-lcci/
'''


from typing import List
import random


class Solution:
    def smallestK1(self, arr: List[int], k: int) -> List[int]:
        return 0
        # 自己写，作弊了呀
        # 1. 排序
        # https://leetcode-cn.com/problems/smallest-k-lcci/solution/zui-xiao-kge-shu-by-leetcode-solution-o5eg/
        # arr.sort()
        # return arr[:k]
        # 时间复杂度：O(nlogn)，其中 n 是数组 arr 的长度。算法的时间复杂度即排序的时间复杂度。
        # 空间复杂度：O(logn)，排序所需额外的空间复杂度为 O(logn)。
        # 执行用时：56 ms, 在所有 Python3 提交中击败了89.20 % 的用户
        # 内存消耗：18.9 MB, 在所有 Python3 提交中击败了62.24 % 的用户

        # 2. 堆
        # https://leetcode-cn.com/problems/smallest-k-lcci/solution/zui-xiao-kge-shu-by-leetcode-solution-o5eg/
        # import heapq
        # if k == 0:
        #     return list()
        # hp = [-x for x in arr[:k]]
        # # print('hp', hp)
        # heapq.heapify(hp)  # 将列表转换为堆
        # # print('hp', hp)
        # for i in range(k, len(arr)):
        #     if -hp[0] > arr[i]:
        #         heapq.heappop(hp)
        #         heapq.heappush(hp, -arr[i])
        # # print('hp', hp)
        # ans = [-x for x in hp]
        # return ans
        # 时间复杂度：O(nlogk)，其中 n 是数组 arr 的长度。由于大根堆实时维护前 k 小值，所以插入删除都是 O(logk) 的时间复杂度，最坏情况下数组里 n 个数都会插入，所以一共需要 O(nlogk) 的时间复杂度。
        # 空间复杂度：O(k)，因为大根堆里最多 k 个数。

        # 3. 快排思想 最佳做法
        # https://leetcode-cn.com/problems/smallest-k-lcci/solution/zui-xiao-kge-shu-by-leetcode-solution-o5eg/
        # https://leetcode-cn.com/leetbook/read/illustration-of-algorithm/55bvvv/
    def partition(self, nums, l, r):
        pivot = nums[r]
        i = l - 1
        for j in range(l, r):
            if nums[j] <= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1], nums[r] = nums[r], nums[i + 1]
        return i + 1

    def randomized_partition(self, nums, l, r):
        i = random.randint(l, r)
        nums[r], nums[i] = nums[i], nums[r]
        return self.partition(nums, l, r)

    def randomized_selected(self, arr, l, r, k):
        pos = self.randomized_partition(arr, l, r)
        num = pos - l + 1
        if k < num:
            self.randomized_selected(arr, l, pos - 1, k)
        elif k > num:
            self.randomized_selected(arr, pos + 1, r, k - num)

    def smallestK(self, arr: List[int], k: int) -> List[int]:
        if k == 0:
            return list()
        self.randomized_selected(arr, 0, len(arr) - 1, k)
        return arr[:k]


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([1, 3, 5, 7, 2, 4, 6, 8], 4, [1, 2, 3, 4]),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.smallestK(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)

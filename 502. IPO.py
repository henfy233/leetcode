# -*- encoding: utf-8 -*-
'''
@File    :   502. IPO.py
@Time    :   2021/09/09 21:58:57
@Author  :   henfy
@Diffi   :   Hard
@Version :   1.0

题目：https://leetcode-cn.com/problems/ipo/
'''


from typing import List
import heapq


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # 看到困难题，就虚了，这能过前两个样例
        # 没解决，项目不能重新取
        # num = 0
        # sum = 0
        # while num < k:
        #     max = 0
        #     arr = []
        #     for i in range(len(capital)):
        #         if w >= capital[i]:
        #             arr.append(i)
        #     print('arr', arr)
        #     for i in arr:
        #         if max < profits[i]:
        #             max = profits[i]
        #     w = max
        #     sum += w
        #     num += 1
        # print('sum', sum)
        # return sum

        # 1. 利用堆的贪心算法
        # https://leetcode-cn.com/problems/ipo/solution/ipo-by-leetcode-solution-89zm/
        # 如果初始资本 w≥max(capital)，我们直接返回利润中的 k 个最大元素的和即可。
        if w >= max(capital):
            return w + sum(heapq.nlargest(k, profits))

        n = len(profits)
        curr = 0
        arr = [(capital[i], profits[i]) for i in range(n)]
        arr.sort(key=lambda x: x[0])

        pq = []
        for _ in range(k):
            while curr < n and arr[curr][0] <= w:
                heapq.heappush(pq, -arr[curr][1])
                curr += 1

            if pq:
                w -= heapq.heappop(pq)
            else:
                break

        return w
        # 时间复杂度：O((n+k)logn)，其中 n 是数组 profits 和 capital 的长度，k 表示最多的选择数目。我们需要 O(nlogn) 的时间复杂度来来创建和排序项目，往堆中添加元素的时间不超过 O(nlogn)，每次从堆中取出最大值并更新资本的时间为 O(klogn)，因此总的时间复杂度为 O(nlogn+nlogn+klogn) = O((n+k)logn)。
        # 空间复杂度：O(n)，其中 n 是数组 profits 和 capital 的长度。空间复杂度主要取决于创建用于排序的数组和大根堆。
        # 执行用时：112 ms, 在所有 Python3 提交中击败了79.78 % 的用户
        # 内存消耗：35.3 MB, 在所有 Python3 提交中击败了51.31 % 的用户


if __name__ == '__main__':
    s = Solution()
    test_list = [
        (2, 0, [1, 2, 3], [0, 1, 1], 4),
        (3, 0, [1, 2, 3], [0, 1, 2], 6),
        (10, 0, [1, 2, 3], [0, 1, 2], 6),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.findMaximizedCapital(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)

# -*- encoding: utf-8 -*-
'''
@File    :   881. 救生艇.py
@Time    :   2021/08/26 01:28:16
@Author  :   henfy
@Diffi   :   Medium
@Version :   1.0

题目：https://leetcode-cn.com/problems/boats-to-save-people/
'''
from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # 自己做，做了半小时，还可以 和官方答案差不多
        # ans = 0
        # n = len(people)
        # left, right = 0, n-1
        # people.sort()
        # while left <= right:
        #     while left < right and people[right] == limit:
        #         ans += 1
        #         right -= 1
        #     while left < right and people[left]+people[right] <= limit:
        #         ans += 1
        #         left += 1
        #         right -= 1
        #     if left <= right and people[right] < limit:
        #         ans += 1
        #         right -= 1
        # return ans
        # 执行用时：92 ms, 在所有 Python3 提交中击败了97.09 % 的用户
        # 内存消耗：20 MB, 在所有 Python3 提交中击败了48.99 % 的用户

        # 1. 贪心
        # https://leetcode-cn.com/problems/boats-to-save-people/solution/jiu-sheng-ting-by-leetcode-solution-0nsp/
        ans = 0
        people.sort()
        light, heavy = 0, len(people) - 1
        while light <= heavy:
            if people[light] + people[heavy] > limit:
                heavy -= 1
            else:
                light += 1
                heavy -= 1
            ans += 1
        return ans
        # 复杂度分析
        # 时间复杂度：O(nlogn)，其中 n 是数组 people 的长度。算法的时间开销主要在排序上。
        # 空间复杂度：O(logn)，排序所需额外的空间复杂度为 O(logn)。


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([1, 2], 3, 1),
        ([3, 2, 2, 1], 3, 3),
        ([3, 5, 3, 4], 5, 4),
        ([7, 3, 2], 8, 2)
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.numRescueBoats(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)

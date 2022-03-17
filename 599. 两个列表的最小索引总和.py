# -*- encoding: utf-8 -*-
'''
@File    :   599. 两个列表的最小索引总和.py
@Time    :   2022/03/14 16:43:40
@Author  :   henfy
@Diffi   :   Easy
@Version :   1.0

题目：https://leetcode-cn.com/problems/minimum-index-sum-of-two-lists/
'''


from math import inf
from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        # 不想做
        # dict = {}
        # n, m = len(list1), len(list2)
        # x = max(n, m)
        # mi = 0
        # ans = []
        # for i in range(x):
        #     if i < n:
        #         if list1[i] in dict:
        #             dict[list1[i]] += i
        #             ans.append(list1[i])
        #             mi = dict[list1[i]]
        #         else:
        #             dict[list1[i]] = i
        #     if i < m:
        #         if list2[i] in dict:
        #             ans.append(list2[i])
        #             dict[list2[i]] += i
        #         else:
        #             dict[list2[i]] = i
        # return ans

        index = {s: i for i, s in enumerate(list1)}
        ans = []
        indexSum = inf
        for i, s in enumerate(list2):
            if s in index:
                j = index[s]
                if i + j < indexSum:
                    indexSum = i + j
                    ans = [s]
                elif i + j == indexSum:
                    ans.append(s)
        return ans


if __name__ == '__main__':
    s = Solution()
    test_list = [
        (["Shogun", "Tapioca Express", "Burger King", "KFC"], [
         "Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"], ["Shogun"]),
        (["Shogun", "Tapioca Express", "Burger King", "KFC"],
         ["KFC", "Shogun", "Burger King"], ["Shogun"]),
        (["Shogun", "Tapioca Express", "Burger King", "KFC"], ["KFC", "Burger King",
         "Tapioca Express", "Shogun"], ["KFC", "Burger King", "Tapioca Express", "Shogun"])
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.findRestaurant(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)

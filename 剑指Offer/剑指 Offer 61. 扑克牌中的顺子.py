# -*- encoding: utf-8 -*-
'''
@File    :   剑指 Offer 61. 扑克牌中的顺子.py
@Time    :   2022/05/24 16:51:38
@Author  :   henfy
@Diffi   :   Easy
@Method  :   排序（简单）

题目：https://leetcode.cn/problems/bu-ke-pai-zhong-de-shun-zi-lcof/
'''


from typing import List


class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        # 集合 Set + 遍历
        repeat = set()
        ma, mi = 0, 14
        for num in nums:
            if num == 0:
                continue  # 跳过大小王
            ma = max(ma, num)  # 最大牌
            mi = min(mi, num)  # 最小牌
            if num in repeat:
                return False  # 若有重复，提前返回 false
            repeat.add(num)  # 添加牌至 Set
        return ma - mi < 5  # 最大牌 - 最小牌 < 5 则可构成顺子

        # 排序 + 遍历
        # joker = 0
        # nums.sort()  # 数组排序
        # for i in range(4):
        #     if nums[i] == 0:
        #         joker += 1  # 统计大小王数量
        #     elif nums[i] == nums[i + 1]:
        #         return False  # 若有重复，提前返回 false
        # return nums[4] - nums[joker] < 5  # 最大牌 - 最小牌 < 5 则可构成顺子


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([1, 2, 3, 4, 5], True),
        ([0, 0, 1, 2, 5], True)
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.isStraight(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)

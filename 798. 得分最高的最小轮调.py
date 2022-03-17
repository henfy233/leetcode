# -*- encoding: utf-8 -*-
'''
@File    :   798. 得分最高的最小轮调.py
@Time    :   2022/03/09 00:39:43
@Author  :   henfy
@Diffi   :   Hard
@Version :   1.0

题目：https://leetcode-cn.com/problems/smallest-rotation-with-highest-score/
'''


from typing import List


class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        # 遇到困难睡大觉
        # 差分数组
        n = len(nums)
        diffs = [0] * n
        for i, num in enumerate(nums):
            low = (i + 1) % n
            high = (i - num + n + 1) % n
            diffs[low] += 1
            diffs[high] -= 1
            if low >= high:
                diffs[0] += 1
        score, maxScore, idx = 0, 0, 0
        for i, diff in enumerate(diffs):
            score += diff
            if score > maxScore:
                maxScore, idx = score, i
        return idx

    def sPrint(x: str):
        print('x', x)


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([2, 3, 1, 4, 0], 3),
        ([1, 3, 0, 2, 4], 0),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.bestRotation(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)

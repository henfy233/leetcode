# -*- encoding: utf-8 -*-
'''
@File    :   517. 超级洗衣机.py
@Time    :   2021/09/29 20:55:29
@Author  :   henfy
@Diffi   :   Hard
@Version :   1.0

题目：https://leetcode-cn.com/problems/super-washing-machines/
'''


from typing import List


class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        # 1. 贪心
        # https://leetcode-cn.com/problems/super-washing-machines/solution/chao-ji-xi-yi-ji-by-leetcode-solution-yhej/
        tot = sum(machines)
        n = len(machines)
        if tot % n:
            return -1
        avg = tot // n
        ans, s = 0, 0
        for num in machines:
            num -= avg
            s += num
            ans = max(ans, abs(s), num)
        return ans


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([1, 0, 5], 3),
        ([0, 3, 0], 2),
        ([0, 2, 0], -1),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.findMinMoves(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)

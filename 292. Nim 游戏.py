# -*- encoding: utf-8 -*-
'''
@File    :   292. Nim 游戏.py
@Time    :   2021/09/18 00:46:08
@Author  :   henfy
@Diffi   :   Easy
@Version :   1.0

题目：https://leetcode-cn.com/problems/nim-game/
'''


# 数学题 我以为是博弈题，不会做
class Solution:
    def canWinNim(self, n: int) -> bool:
        # 1. 数学推理
        # https://leetcode-cn.com/problems/nim-game/solution/nim-you-xi-by-leetcode-solution-95g8/
        return n % 4 != 0


if __name__ == '__main__':
    s = Solution()
    test_list = [
        (4, False),
        (1, True),
        (2, True),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.canWinNim(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)

# -*- encoding: utf-8 -*-
'''
@File    :   3. 黑白翻转棋.py
@Time    :   2021/09/11 15:30:38
@Author  :   henfy
@Diffi   :   Medium
@Version :   1.0

题目：https://leetcode-cn.com/contest/season/2021-fall/problems/fHi6rV/
'''


from typing import List


class Solution:
    def flipChess(self, chessboard: List[str]) -> int:


if __name__ == '__main__':
    s = Solution()
    test_list = [
        (["....X.", "....X.", "XOOO..", "......", "......"], 3),
        ([".X.", ".O.", "XO."], 2),
        ([".......", ".......", ".......", "X......",
         ".O.....", "..O....", "....OOX"], 4),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.flipChess(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)

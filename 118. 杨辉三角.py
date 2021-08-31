# -*- encoding: utf-8 -*-
'''
@File    :   118. 杨辉三角.py
@Time    :   2021/08/28 00:43:32
@Author  :   henfy
@Diffi   :   Easy
@Version :   1.0

题目：https://leetcode-cn.com/problems/pascals-triangle/
'''


from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # 自己写，还算简单
        # ans = [[1]*i for i in range(1, numRows+1)]
        # for i in range(2, numRows):
        #     for j in range(1, len(ans[i])-1):
        #         ans[i][j] = ans[i-1][j-1] + ans[i-1][j]
        # return ans
        # 执行用时：32 ms, 在所有 Python3 提交中击败了70.74 % 的用户
        # 内存消耗：14.8 MB, 在所有 Python3 提交中击败了93.53 % 的用户

        # 1. 数学
        # https://leetcode-cn.com/problems/pascals-triangle/solution/yang-hui-san-jiao-by-leetcode-solution-lew9/
        ret = list()
        for i in range(numRows):
            row = list()
            for j in range(0, i + 1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(ret[i - 1][j] + ret[i - 1][j - 1])
            ret.append(row)
        return ret
        # 复杂度分析
        # 时间复杂度：O(numRows ^ 2)。
        # 空间复杂度：O(1)。不考虑返回值的空间占用。
        # 执行用时：28 ms, 在所有 Python3 提交中击败了88.49 % 的用户
        # 内存消耗：14.9 MB, 在所有 Python3 提交中击败了57.79 % 的用户


if __name__ == '__main__':
    s = Solution()
    test_list = [
        (5, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]),
        (1, [[1]]),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.generate(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)

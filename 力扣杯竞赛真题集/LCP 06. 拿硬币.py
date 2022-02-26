# -*- encoding: utf-8 -*-
'''
@File    :   LCP 06. 拿硬币.py
@Time    :   2021/09/01 13:27:29
@Author  :   henfy
@Diffi   :   Easy
@Version :   1.0

题目：https://leetcode-cn.com/problems/na-ying-bi/
'''


from typing import List


class Solution:
    def minCount(self, coins: List[int]) -> int:
        # 自己做，这题简单
        # sum = 0
        # for i in range(len(coins)):
        #     if coins[i] % 2:
        #         sum += 1
        #     sum += coins[i]//2
        #     # print(sum)
        # return sum
        # 执行用时：36 ms, 在所有 Python3 提交中击败了58.21 % 的用户
        # 内存消耗：14.8 MB, 在所有 Python3 提交中击败了70.57 % 的用户

        # 1. 贪心
        # https://leetcode-cn.com/problems/na-ying-bi/solution/na-ying-bi-by-leetcode-solution/
        return sum([(x+1)//2 for x in coins])
        # 时间复杂度：O(n)。
        # 空间复杂度：O(n)。


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([4, 2, 1], 4),
        ([2, 3, 10], 8),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.minCount(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)

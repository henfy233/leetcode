# -*- encoding: utf-8 -*-
'''
@File    :   191. 位1的个数.py
@Time    :   2021/08/27 19:32:44
@Author  :   henfy
@Diffi   :   Easy
@Version :   1.0

题目：https://leetcode-cn.com/problems/number-of-1-bits/
'''


class Solution:
    def hammingWeight(self, n: int) -> int:
        # 自己想，但是还能优化
        # s = str(bin(n))
        # sum = 0
        # # print(s)
        # for i in s:
        #     if i == '1':
        #         sum += 1
        # return sum
        # 执行用时：36 ms, 在所有 Python3 提交中击败了59.74 % 的用户
        # 内存消耗：14.8 MB, 在所有 Python3 提交中击败了64.73 % 的用户

        # 1. 循环检查二进制位
        # https://leetcode-cn.com/problems/number-of-1-bits/solution/wei-1de-ge-shu-by-leetcode-solution-jnwf/
        ret = sum(1 for i in range(32) if n & (1 << i))
        return ret
        # 复杂度分析
        # 时间复杂度：O(k)，其中 k 是 int 型的二进制位数，k = 32。我们需要检查 n 的二进制位的每一位，一共需要检查 32 位。
        # 空间复杂度：O(1)，我们只需要常数的空间保存若干变量。

        # 2. 位运算优化
        # https://leetcode-cn.com/problems/number-of-1-bits/solution/wei-1de-ge-shu-by-leetcode-solution-jnwf/
        # ret = 0
        # while n:
        #     n &= n - 1
        #     ret += 1
        # return ret
        # 复杂度分析
        # 时间复杂度：O(logn)。循环次数等于 n 的二进制位中 1 的个数，最坏情况下 n 的二进制位全部为 1。我们需要循环 logn 次。
        # 空间复杂度：O(1)，我们只需要常数的空间保存若干变量。

# -*- encoding: utf-8 -*-
'''
@File    :   190. 颠倒二进制位.py
@Time    :   2021/08/27 23:15:46
@Author  :   henfy
@Diffi   :   Easy
@Version :   1.0

题目：https://leetcode-cn.com/problems/reverse-bits/
'''


class Solution:
    def reverseBits(self, n: int) -> int:
        # 自己写，研究之前自己写的，数组转字符串不会
        # s = bin(n)[2:]
        # x = ['0']*(32-len(s))+list(s)
        # head, tail = 0, len(x)-1
        # while head < tail:
        #     x[head], x[tail] = x[tail], x[head]
        #     head += 1
        #     tail -= 1
        # return int(''.join(x), 2)  # 十进制 转 二进制
        # 执行用时：44 ms, 在所有 Python3 提交中击败了24.01 % 的用户
        # 内存消耗：14.7 MB, 在所有 Python3 提交中击败了90.98 % 的用户

        # 1. 逐位颠倒
        # https://leetcode-cn.com/problems/reverse-bits/solution/dian-dao-er-jin-zhi-wei-by-leetcode-solu-yhxz/
        # rev = 0
        # for i in range(32):
        #     if n != 0:
        #         rev |= (n & 1) << (31 - i)
        #         n >>= 1
        # return rev
        # 复杂度分析
        # 时间复杂度：O(logn)。
        # 空间复杂度：O(1)。

        # 2. 位运算分治
        # https://leetcode-cn.com/problems/reverse-bits/solution/fu-xue-ming-zhu-xun-huan-yu-fen-zhi-jie-hoakf/
        n = (n >> 16) | (n << 16)
        n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8)
        n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4)
        n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2)
        n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1)
        return n
        # 复杂度分析
        # 时间复杂度：O(1)。
        # 空间复杂度：O(1)。


# 00000010100101000001111010011100
# 11111111111111111111111111111101
# 00000010100101000001111010011100
# 11111111111111111111111111111101

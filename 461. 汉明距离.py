# -*- encoding: utf-8 -*-
'''
@File    :   汉明距离.py
@Time    :   2021/08/27 19:36:03
@Author  :   henfy
@Diffi   :   Easy
@Version :   1.0

题目：https://leetcode-cn.com/problems/hamming-distance/
'''


# 推荐 1 2方法
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # 自己写，不通过
        # x = list(bin(x))[2:]
        # y = list(bin(y))[2:]
        # ans = 0
        # print('x', x)
        # print('y', y)
        # for i in range(len(x)):
        #     if x[i] != y[i]:
        #         ans += 1
        # return ans

        # 1. 移位实现位计数
        # https://leetcode-cn.com/problems/hamming-distance/solution/yi-ming-ju-chi-by-leetcode-solution-u1w7/
        s, ret = x ^ y, 0
        # print('s', s)
        while s != 0:
            ret += s & 1
            s >>= 1
        return ret
        # 复杂度分析
        # 时间复杂度：O(logC)，其中 CC 是元素的数据范围，在本题中 logC = log2^31=31。
        # 空间复杂度：O(1)。

        # 2. Brian Kernighan 算法
        # s, ret = x ^ y, 0
        # while s != 0:
        #     s &= s-1
        #     ret += 1
        # return ret
        # 时间复杂度：O(logC)，其中 CC 是元素的数据范围，在本题中 logC = log2^31=31。
        # 空间复杂度：O(1)。

        # 3. 逐位比较
        # ans = 0
        # for i in range(32):
        #     a = (x >> i) & 1
        #     b = (y >> i) & 1
        #     ans += a ^ b
        # return ans

        # 4. python API
        # return bin(x ^ y).count('1')


if __name__ == '__main__':
    s = Solution()
    test_list = [
        (1, 4, 2),
        (3, 1, 1),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.hammingDistance(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)

#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   计数质数.py
@Time    :   2021/08/03 23:12:08
@Author  :   henfy
@Version :   1.0
'''

# here put the import lib


# 难题，之前做过，现在一脸懵逼
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 1. 使用标准的 埃拉托斯特尼 埃氏筛选法
        isNumPrimes = [True] * n  # 将所有数，展开所有数 标记质数真
        count = 0  # 质数计数器 因为1不是质数 所以 0
        # 遍历 2-n数，判断是否是质数，从 2开始对应-质数3 [1,2,3]  1不算质数
        for i in range(2, n):
            if isNumPrimes[i]:
                count += 1
                # 使用埃拉托斯特尼 筛选法进行过滤 将合数去除
                for j in range(i*i, n, i):  # 遍历 i*i  2倍i值 开始，结束n, 步数i (倍数递增)
                    isNumPrimes[j] = False  # 把合数置为 False
        return count
        # 执行用时：1176 ms, 在所有 Python 提交中击败了73.90 % 的用户
        # 内存消耗：283.8 MB, 在所有 Python 提交中击败了20.58 % 的用户

        # 2. 普通的方法 超出时间限制
        # count = 0
        # if n <= 2:
        #     return 0
        # else:
        #     for i in range(3, n):
        #         isTrue = True
        #         for j in range(2, i):
        #             if i % j == 0:
        #                 isTrue = False
        #                 break
        #         if isTrue:
        #             count += 1
        # return count + 1


if __name__ == '__main__':
    s = Solution()
    test_list = [
        (10, 4),
        (0, 0),
        (1, 0),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.countPrimes(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)

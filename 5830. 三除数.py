#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   5830. 三除数.py
@Time    :   2021/08/01 23:58:05
@Author  :   henfy
@Version :   1.0
'''

# here put the import lib


class Solution(object):
    def isThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 自己做 比较简单
        # count = 0
        # for i in range(2, n):
        #     if n % i == 0:
        #         count += 1
        # if count == 1:
        #     return True
        # else:
        #     return False

        # 1. 枚举正除数
        cnt = 0
        i = 1
        while i * i <= n:
            if n % i == 0:
                if i != n // i:
                    # 此时 i 与 n / i 为不同整数
                    cnt += 2
                else:
                    # 此时 i 与 n / i 相等
                    cnt += 1
            i += 1
        return cnt == 3


if __name__ == '__main__':
    s = Solution()
    test_list = [
        (2, False),
        (4, True),
        (6, False),
        (9, True),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.isThree(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)

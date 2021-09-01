# -*- encoding: utf-8 -*-
'''
@File    :   165. 比较版本号.py
@Time    :   2021/09/01 01:16:33
@Author  :   henfy
@Diffi   :   Medium
@Version :   1.0

题目：https://leetcode-cn.com/problems/compare-version-numbers/
'''


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # 自己做，这题还行
        v1, v2 = version1.split('.'), version2.split('.')
        m, n = len(v1), len(v2)
        i = 0
        if m > n:
            v2 += ['0']*(m-n)
            n = len(v2)
        else:
            v1 += ['0']*(n-m)
            m = len(v1)
        while i < m and i < n:
            if int(v1[i]) > int(v2[i]):
                return 1
            elif int(v1[i]) < int(v2[i]):
                return -1
            else:
                i += 1
        return 0
        # 执行用时：32 ms, 在所有 Python3 提交中击败了74.56 % 的用户
        # 内存消耗：15 MB, 在所有 Python3 提交中击败了54.53 % 的用户

        # 1. 字符串分割
        # https://leetcode-cn.com/problems/compare-version-numbers/solution/bi-jiao-ban-ben-hao-by-leetcode-solution-k6wi/
        # from itertools import zip_longest
        # for v1, v2 in zip_longest(version1.split('.'), version2.split('.'), fillvalue=0):
        #     x, y = int(v1), int(v2)
        #     if x != y:
        #         return 1 if x > y else -1
        # return 0
        # 时间复杂度：O(n+m)（或 O(max(n, m))，这是等价的），其中 n 是字符串 version1 的长度，m 是字符串 version2 的长度。
        # 空间复杂度：O(n+m)，我们需要 O(n+m) 的空间存储分割后的修订号列表。

        # 2. 双指针
        # https://leetcode-cn.com/problems/compare-version-numbers/solution/bi-jiao-ban-ben-hao-by-leetcode-solution-k6wi/
        # 1.0.0.0.0和1没有区别，除非后面有个大于0的一位，我们要一直比较到出现大小差异的那位，否则他们相等。
        # n, m = len(version1), len(version2)
        # i, j = 0, 0
        # while i < n or j < m:
        #     x = 0
        #     while i < n and version1[i] != '.':
        #         x = x * 10 + ord(version1[i]) - ord('0')
        #         i += 1
        #     i += 1  # 跳过点号
        #     y = 0
        #     while j < m and version2[j] != '.':
        #         y = y * 10 + ord(version2[j]) - ord('0')
        #         j += 1
        #     j += 1  # 跳过点号
        #     if x != y:
        #         return 1 if x > y else -1
        # return 0
        # 时间复杂度：O(n+m)，其中 nn 是字符串 version1 的长度，m 是字符串 version2 的长度。
        # 空间复杂度：O(1)，我们只需要常数的空间保存若干变量。


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ("1.01", "1.001", 0),
        ("1.01", "1.001", 0),
        ("0.1", "1.1", -1),
        ("1.0.1", "1", 1),
        ("7.5.2.4", "7.5.3", -1),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.compareVersion(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)

# -*- encoding: utf-8 -*-
'''
@File    :   1894. 找到需要补充粉笔的学生编号.py
@Time    :   2021/09/10 10:17:53
@Author  :   henfy
@Diffi   :   Medium
@Version :   1.0

题目：https://leetcode-cn.com/problems/find-the-student-that-will-replace-the-chalk/
'''


from typing import List
import bisect


class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        # 自己写
        # total = sum(chalk)
        # print('total', total)
        # k %= total
        # print('k', k)
        # while True:
        #     for i, x in enumerate(chalk):
        #         k -= x
        #         if k < 0:
        #             return i
        # 执行用时：64 ms, 在所有 Python3 提交中击败了90.88 % 的用户
        # 内存消耗：24.3 MB, 在所有 Python3 提交中击败了96.65 % 的用户

        # 1. 优化的模拟
        # https://leetcode-cn.com/problems/find-the-student-that-will-replace-the-chalk/solution/zhao-dao-xu-yao-bu-chong-fen-bi-de-xue-s-qrn1/
        # total = sum(chalk)
        # k %= total
        # res = -1
        # for i, cnt in enumerate(chalk):
        #     if cnt > k:
        #         res = i
        #         break
        #     k -= cnt
        # return res
        # 时间复杂度：O(n)，其中 n 是数组 chalk 的长度。我们最多遍历数组 chalk 两次，第一次求出粉笔的总量 total，第二次找出答案。
        # 空间复杂度：O(1)。

        # 2. 前缀和 + 二分查找
        n = len(chalk)
        if chalk[0] > k:
            return 0
        for i in range(1, n):
            chalk[i] += chalk[i - 1]
            if chalk[i] > k:
                return i
        k %= chalk[-1]
        return bisect.bisect_right(chalk, k)
        # 时间复杂度：O(n)，其中 n 是数组 chalk 的长度。计算前缀和的时间复杂度为 O(n)，二分查找的时间复杂度为 O(logn)，因此总时间复杂度为 O(n)。
        # 空间复杂度：O(1)。


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([5, 1, 5], 22, 0),
        ([3, 4, 1, 2], 25, 1),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.chalkReplacer(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)

# -*- encoding: utf-8 -*-
'''
@File    :   278. 第一个错误的版本.py
@Time    :   2021/08/31 18:25:38
@Author  :   henfy
@Diffi   :   Easy
@Version :   1.0

题目：https://leetcode-cn.com/problems/first-bad-version/
'''

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer


def isBadVersion(version):
    return 0


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 自己写，上下限区间有问题，不知取上还是取下
        # 参考下面的做法，基本一样
        left, right = 1, n
        while left < right:
            mid = left + (right-left)/2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left
        # 执行用时：36 ms, 在所有 Python3 提交中击败了52.56 % 的用户
        # 内存消耗：14.9 MB, 在所有 Python3 提交中击败了24.50 % 的用户

        # 1. 二分查找
        # https://leetcode-cn.com/problems/first-bad-version/solution/di-yi-ge-cuo-wu-de-ban-ben-by-leetcode-s-pf8h/
        # left, right = 1, n
        # while left < right:  # 循环直至区间左右端点相同
        #     mid = left + (right - left) / 2
        #     # 防止计算时溢出
        #     if isBadVersion(mid):
        #         right = mid
        #         # 答案在区间[left, mid] 中
        #     else:
        #         left = mid + 1
        #         # 答案在区间[mid+1, right] 中
        # # 此时有 left == right，区间缩为一个点，即为答案
        # return left
        # 时间复杂度：O(logn)，其中 n 是给定版本的数量。
        # 空间复杂度：O(1)。我们只需要常数的空间保存若干变量。


# if __name__ == '__main__':
#     s = Solution()
#     test_list = [
#         (5, 4, 4),
#         (1, 1, 1),
#     ]

#     for test_index, test_case in enumerate(test_list, start=1):
#         *test, result = test_case
#         test_result = s.firstBadVersion(*test)
#         if test_result != result:
#             raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
#                 test_index, result, test_result))
#         print("test_case %d succeed." % test_index)

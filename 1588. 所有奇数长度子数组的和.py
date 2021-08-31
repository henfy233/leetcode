# -*- encoding: utf-8 -*-
'''
@File    :   1588. 所有奇数长度子数组的和.py
@Time    :   2021/08/29 00:42:32
@Author  :   henfy
@Diffi   :   Easy
@Version :   1.0

题目：https://leetcode-cn.com/problems/sum-of-all-odd-length-subarrays/
'''


from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        # 自己写，突然就做对了
        # n = len(arr)
        # ans = 0
        # for x in range(1, n+1, 2):
        #     for i in range(n-x+1):
        #         ans += sum(arr[i:i+x])
        # return ans
        # 时间复杂度是 O(n ^ 3)
        # 执行用时：44 ms, 在所有 Python3 提交中击败了79.93 % 的用户
        # 内存消耗：15 MB, 在所有 Python3 提交中击败了30.10 % 的用户

        # 使用前缀和（Prefix Sum）的方式。
        # 使用 O(n) 的时间可以预处理前缀和数组，之后使用 O(1) 的时间即可计算出一个连续子数组的和
        # https://leetcode-cn.com/problems/sum-of-all-odd-length-subarrays/solution/python-jian-dan-qian-zhui-he-by-dangerusswilson/
        # n = len(arr)
        # pre = [0]
        # for num in arr:
        #     pre.append(pre[-1] + num)
        # res = 0
        # for l in range(1, n+1, 2):
        #     for i in range(0, n+1-l):
        #         res += pre[i+l] - pre[i]
        # return res
        # 时间复杂度是 O(n ^ 2) 的，空间复杂度是 O(n) 的

        # 这个想的头有点炸
        # 这个问题有 O(n) 的解法。
        # https: // leetcode-cn.com/problems/sum-of-all-odd-length-subarrays/solution/cong-on3-dao-on-de-jie-fa-by-liuyubobobo/
        res = 0
        for i in range(len(arr)):
            left = i + 1
            right = len(arr) - i
            left_even = (left + 1) // 2
            right_even = (right + 1) // 2
            left_odd = left // 2
            right_odd = right // 2
            print('arr[i]', arr[i])
            print('left_even', left_even)
            print('right_even', right_even)
            print('left_odd', left_odd)
            print('right_odd', right_odd)
            res += (left_even * right_even + left_odd * right_odd) * arr[i]
        return res
        # 执行用时：32 ms, 在所有 Python3 提交中击败了96.27 % 的用户
        # 内存消耗：14.8 MB, 在所有 Python3 提交中击败了86.44 % 的用户


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([1, 4, 2, 5, 3], 58),
        # ([1, 2], 3),
        # ([10, 11, 12], 66),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.sumOddLengthSubarrays(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)

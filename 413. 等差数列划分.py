#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   413. 等差数列划分.py
@Time    :   2021/08/10 01:12:51
@Author  :   henfy
@Diffi   :   middle
@Version :   1.0

如果一个数列 至少有三个元素 ，并且任意两个相邻元素之差相同，则称该数列为等差数列。
 - 例如，[1,3,5,7,9]、[7,7,7,7] 和 [3,-1,-5,-9] 都是等差数列。

给你一个整数数组 nums ，返回数组 nums 中所有为等差数组的 子数组 个数。

子数组 是数组中的一个连续序列。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/arithmetic-slices
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib


# woc，一看又是不会的题，果然看了答案，不会
# 看完答案，发现又不是很难，淦
class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 1. 差分 + 计数
        # 思路与算法
        # 考虑一个比较直观的做法：
        # - 我们枚举等差数列的最后两项 nums[i−1] 以及 nums[i]，那么等差数列的公差 d 即为 nums[i−1]−nums[i]；
        # - 随后我们使用一个指针 j 从 i - 2 开始逆序地遍历数组的前缀部分 nums[0..i−2]：
        # - - 如果 nums[j]−nums[j+1] = d，那么说明 nums[j], ⋯, nums[i] 组成了一个长度至少为 3 的等差数列，答案增加 1；
        # - - 否则更小的 j 也无法作为等差数列的首个位置了，我们直接退出遍历。
        # 这个做法的时间复杂度是 O(n ^ 2)的，即枚举最后两项的时间复杂度为 O(n)，使用指针 j 遍历的时间复杂度也为 O(n)，相乘得到总时间复杂度 O(n ^ 2)。对于一些运行较慢的语言，该方法可能会超出时间限制，因此我们需要进行优化。
        n = len(nums)
        if n == 1:
            return 0
        d, t = nums[0] - nums[1], 0
        ans = 0
        # 因为等差数列的长度至少为 3，所以可以从 i=2 开始枚举
        for i in range(2, n):
            if nums[i - 1] - nums[i] == d:
                t += 1
            else:
                d = nums[i - 1] - nums[i]
                t = 0
            ans += t
        return ans
        # 复杂度分析
        # 时间复杂度：O(n)，其中 nn 是数组 nums 的长度。
        # 空间复杂度：O(1)。

        # 2. 其他做法
        # 首先遍历原数组 nums，用数组 diffs 存储相邻两个元素之间的差值。
        # 然后遍历 diffs，用数组 cons 存储其中连续相同的差值的数目，比如有 3 个 3 连在一起，意味着原数组中这个位置存在一个最大长度为 4 的等差数列。
        # 然后遍历 cons，对于长度为 n 的等差数列，其所有的长度大于等于 3 的子数列都是等差数列，则一共有(n-2)(n-1)/2 个等差数列。
        # 全部相加得到结果。
        # 第一次遍历
    #     diffs = []
    #     for i in range(len(nums) - 1):
    #         diffs.append(nums[i + 1] - nums[i])
    #     # 第二次遍历
    #     cons = []
    #     a = 1
    #     for i in range(1, len(diffs)):
    #         if diffs[i] == diffs[i - 1]:
    #             a += 1
    #         else:
    #             cons.append(a)
    #             a = 1
    #     cons.append(a)
    #     # 第三次遍历
    #     res = 0
    #     for num in cons:
    #         res += int(self.calc(num))
    #     return res

    # # 用于计算cons内每个数代表的等差数列个数
    # def calc(self, n):
    #     if n == 1:
    #         return 0
    #     n += 1
    #     return (n-2)*(n-1)/2


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([1, 2, 3, 4], 3),
        ([1], 0),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.numberOfArithmeticSlices(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)

# -*- encoding: utf-8 -*-
'''
@File    :   1646. 获取生成数组中的最大值.py
@Time    :   2021/08/23 00:20:52
@Author  :   henfy
@Diffi   :   Easy
@Version :   1.0

https://leetcode-cn.com/problems/get-maximum-in-generated-array/
'''


class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        # 1. 自己写
        # if n == 0:
        #     return 0
        # nums = [0]*(n+1)
        # nums[1] = 1
        # for i in range(2, n+1):
        #     if i % 2 == 0:
        #         nums[i] = nums[i//2]
        #     else:
        #         nums[i] = nums[i//2] + nums[i//2 + 1]
        # return max(nums)
        # 执行用时：32 ms, 在所有 Python3 提交中击败了74.57 % 的用户
        # 内存消耗：14.7 MB, 在所有 Python3 提交中击败了96.57 % 的用户

        # 2. 模拟
        # 链接：https://leetcode-cn.com/problems/get-maximum-in-generated-array/solution/huo-qu-sheng-cheng-shu-zu-zhong-de-zui-d-0z2l/
        if n == 0:
            return 0
        nums = [0] * (n + 1)
        nums[1] = 1
        for i in range(2, n + 1):
            nums[i] = nums[i // 2] + i % 2 * nums[i // 2 + 1]
        return max(nums)
        # 复杂度分析
        # 时间复杂度：O(n)。
        # 空间复杂度：O(n)。


if __name__ == '__main__':
    s = Solution()
    test_list = [
        (7, 3),
        (2, 1),
        (3, 2),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.getMaximumGenerated(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)

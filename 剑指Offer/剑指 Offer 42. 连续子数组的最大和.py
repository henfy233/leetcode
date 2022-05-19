# -*- encoding: utf-8 -*-
'''
@File    :   剑指 Offer 42. 连续子数组的最大和.py
@Time    :   2022/04/29 13:35:13
@Author  :   henfy
@Diffi   :   Easy
@Version :   1.0

题目：https://leetcode-cn.com/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof/
'''


from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 自己写，效率不好
        # ma = 0
        # sum = 0
        # res = []
        # for num in nums:
        #     sum = max(num, sum+num)
        #     ma = max(sum, num, ma)
        #     # sum = ma
        #     res.append(sum)
        # print('res', res)
        # return max(res)
        '''
        作者：jyd
        链接：https://leetcode-cn.com/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof/solution/mian-shi-ti-42-lian-xu-zi-shu-zu-de-zui-da-he-do-2/
        来源：力扣（LeetCode）
        著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        '''
        # 动态规划
        for i in range(1, len(nums)):
            nums[i] += max(nums[i - 1], 0)
        return max(nums)


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.maxSubArray(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)

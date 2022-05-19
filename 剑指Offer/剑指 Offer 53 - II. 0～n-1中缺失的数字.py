# -*- encoding: utf-8 -*-
'''
@File    :   剑指 Offer 53 - II. 0～n-1中缺失的数字.py
@Time    :   2022/04/25 16:15:05
@Author  :   henfy
@Diffi   :   Easy
@Version :   1.0

题目：https://leetcode-cn.com/problems/que-shi-de-shu-zi-lcof/
'''


from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # 自己写， 二分法
        i, j = 0, len(nums)-1
        while i <= j:
            m = (i+j)//2
            if m == nums[m]:
                i = m+1
            else:
                j = m-1
        return i
        '''
        作者：jyd
        链接：https: // leetcode-cn.com/problems/que-shi-de-shu-zi-lcof/solution/mian-shi-ti-53-ii-0n-1zhong-que-shi-de-shu-zi-er-f/
        来源：力扣（LeetCode）
        著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        '''


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([0, 1, 3], 2),
        ([0, 1, 2, 3, 4, 5, 6, 7, 9], 8),
        ([0, 1, 3, 4, 5, 6, 7, 8, 9], 2),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.missingNumber(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)

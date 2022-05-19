# -*- encoding: utf-8 -*-
'''
@File    :   剑指 Offer 03. 数组中重复的数字.py
@Time    :   2022/04/25 01:30:34
@Author  :   henfy
@Diffi   :   Easy
@Version :   1.0

题目：https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/
'''


from collections import defaultdict
from typing import List


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        # 自己写
        # res = defaultdict(dict)
        # for i, num in enumerate(nums):
        #     # print(i, num)
        #     if num not in res:
        #         res[num] = 1
        #     else:
        #         return num

        # 哈希表 / Set
        # dic = set()
        # for num in nums:
        #     if num in dic:
        #         return num
        #     dic.add(num)
        # return -1

        # 原地交换
        i = 0
        while i < len(nums):
            if nums[i] == i:
                i += 1
                continue
            if nums[nums[i]] == nums[i]:
                return nums[i]
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        return -1
        '''
        作者：jyd
        链接：https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/solution/mian-shi-ti-03-shu-zu-zhong-zhong-fu-de-shu-zi-yua/
        来源：力扣（LeetCode）
        著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        '''


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([2, 3, 1, 0, 2, 5, 3], 2 or 3),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.findRepeatNumber(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)

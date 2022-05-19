# -*- encoding: utf-8 -*-
'''
@File    :   剑指 Offer 11. 旋转数组的最小数字.py
@Time    :   2022/04/25 17:16:32
@Author  :   henfy
@Diffi   :   Easy
@Version :   1.0

题目：https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/
'''


from typing import List


class Solution:
    def minArray(self, numbers: List[int]) -> int:
        # 没想到这都能通过
        # return min(numbers)
        '''
        作者：jyd
        链接：https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/solution/mian-shi-ti-11-xuan-zhuan-shu-zu-de-zui-xiao-shu-3/
        来源：力扣（LeetCode）
        著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        '''
        i, j = 0, len(numbers)-1
        while i <= j:
            m = (i+j)//2
            if numbers[m] < numbers[j]:
                j = m
            elif numbers[m] == numbers[j]:
                j -= 1
            else:
                i = m+1
        return numbers[i]


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([3, 4, 5, 1, 2], 1),
        ([2, 2, 2, 0, 1], 0)
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.minArray(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)

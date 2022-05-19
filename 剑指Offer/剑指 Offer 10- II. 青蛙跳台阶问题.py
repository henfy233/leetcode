# -*- encoding: utf-8 -*-
'''
@File    :   剑指 Offer 10- II. 青蛙跳台阶问题.py
@Time    :   2022/04/29 11:02:59
@Author  :   henfy
@Diffi   :   Easy
@Version :   1.0

题目：https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof/
'''


class Solution:
    def numWays(self, n: int) -> int:
        # arr = [1 for _ in range(n+1)]
        # if n < 2:
        #     return arr[n]
        # arr[2] = 2
        # for i in range(2, n+1):
        #     arr[i] = arr[i-1] + arr[i-2]
        # # print('arr', arr)
        # return arr[-1] % 1000000007
        '''
        作者：jyd
        链接：https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof/solution/mian-shi-ti-10-ii-qing-wa-tiao-tai-jie-wen-ti-dong/
        来源：力扣（LeetCode）
        著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        '''
        a, b = 1, 1
        for _ in range(n):
            a, b = b, a + b
        return a % 1000000007


if __name__ == '__main__':
    s = Solution()
    test_list = [
        (2, 2),
        (7, 21),
        (0, 1),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.numWays(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)

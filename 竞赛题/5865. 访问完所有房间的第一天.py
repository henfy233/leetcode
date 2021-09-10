# -*- encoding: utf-8 -*-
'''
@File    :   5865. 访问完所有房间的第一天.py
@Time    :   2021/09/05 10:56:30
@Author  :   henfy
@Diffi   :   Medium
@Version :   1.0

题目：https://leetcode-cn.com/contest/weekly-contest-257/problems/first-day-where-you-have-been-in-all-the-rooms/
'''


from typing import List


class Solution:
    def firstDayBeenInAllRooms(self, nextVisit: List[int]) -> int:
        # 超出时间限制
        ans = 0
        n = len(nextVisit)
        flag = [0]*n
        next = nextVisit[0]
        # for i in range(n):
        while next < n-1:
            # next = nextVisit[i]
            flag[next] += 1
            if flag[next] % 2:  # 奇数
                next = nextVisit[next]
            else:
                next = (next + 1) % n
            ans += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([0, 0], 2),
        ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, , 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], 2),
        ([0, 0, 2], 6),
        ([0, 1, 2, 0], 6),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.firstDayBeenInAllRooms(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)

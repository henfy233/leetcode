#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   551. 学生出勤记录 I.py
@Time    :   2021/08/17 10:24:25
@Author  :   henfy
@Diffi   :   easy
@Version :   1.0

给你一个字符串 s 表示一个学生的出勤记录，其中的每个字符用来标记当天的出勤情况（缺勤、迟到、到场）。
记录中只含下面三种字符：
 - 'A'：Absent，缺勤
 - 'L'：Late，迟到
 - 'P'：Present，到场

如果学生能够 同时 满足下面两个条件，则可以获得出勤奖励：
 - 按 总出勤 计，学生缺勤（'A'）严格 少于两天。
 - 学生 不会 存在 连续 3 天或 3 天以上的迟到（'L'）记录。
如果学生可以获得出勤奖励，返回 true ；否则，返回 false 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/student-attendance-record-i
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib


class Solution:
    def checkRecord(self, s: str) -> bool:
        # 自己写，这题还是比较简单的，需要规范代码
        # 这题自己写复杂了，唉有点菜
        # countA = 0
        # countL = 0
        # sumL = 0
        # flag = False
        # for i in s:
        #     if i == 'A':
        #         countA += 1
        #         flag = False
        #         if countA > 1:
        #             return False
        #     elif i == 'L':
        #         if flag:
        #             countL += 1
        #             sumL = max(sumL, countL)
        #             if sumL >= 3:
        #                 return False
        #         else:
        #             flag = True
        #             countL = 1
        #     else:
        #         flag = False
        # return True
        # 执行用时：24 ms, 在所有 Python3 提交中击败了99.09 % 的用户
        # 内存消耗：15 MB, 在所有 Python3 提交中击败了17.88 % 的用户

        # 1. 一次遍历
        # 可奖励的出勤记录要求缺勤次数少于 2 和连续迟到次数少于 3。判断出勤记录是否可奖励，只需要遍历出勤记录，判断这两个条件是否同时满足即可。
        # 遍历过程中，记录缺勤次数和连续迟到次数，根据遍历到的字符更新缺勤次数和连续迟到次数：
        #  - 如果遇到 ‘A’，即缺勤，则将缺勤次数加 1，否则缺勤次数不变；
        #  - 如果遇到 ‘L’，即迟到，则将连续迟到次数加 1，否则将连续迟到次数清零。
        # 如果在更新缺勤次数和连续迟到次数之后，出现缺勤次数大于或等于 2 或者连续迟到次数大于或等于 3，则该出勤记录不满足可奖励的要求，返回 false。如果遍历结束时未出现出勤记录不满足可奖励的要求的情况，则返回 true。
        absents = lates = 0
        for _, c in enumerate(s):
            if c == "A":
                absents += 1
                if absents >= 2:
                    return False
            if c == "L":
                lates += 1
                if lates >= 3:
                    return False
            else:
                lates = 0
        return True
        # 复杂度分析
        # 时间复杂度：O(n)，其中 nn 是字符串 s 的长度。需要遍历字符串 s 一次。
        # 空间复杂度：O(1)。
        # 执行用时：32 ms, 在所有 Python3 提交中击败了83.21 % 的用户
        # 内存消耗：15 MB, 在所有 Python3 提交中击败了24.45 % 的用户


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ("PPALLP", True),
        ("PPALLL", False),
        ("PPAALL", False),
        ("LLLL", False)
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.checkRecord(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)

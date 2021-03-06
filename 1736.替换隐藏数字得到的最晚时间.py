# -*- encoding: utf-8 -*-
'''
@File    :   1736.替换隐藏数字得到的最晚时间.py
@Time    :   2021/07/24 02:21:35
@Author  :   henfy
@Diffi   :   Easy
@Version :   1.0

题目：https://leetcode-cn.com/problems/latest-time-by-replacing-hidden-digits/
'''


class Solution(object):
    def maximumTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        # 1. 贪心 + 状态机
        # str = ''
        # if time[0] == '?':
        #     str += '1' if ('4' <= time[1] and time[1] <= '9') else '2'
        # else:
        #     str += time[0]
        # if time[1] == '?':
        #     str += '3' if time[0] > '1' else '9'
        # else:
        #     str += time[1]
        # str += ':'
        # if time[3] == '?':
        #     str += '5'
        # else:
        #     str += time[3]
        # if time[4] == '?':
        #     str += '9'
        # else:
        #     str += time[4]
        # return str

        # sb = []
        # sb.append(time[0] if time[0] != '?' else '2' if time[1]
        #           == '?' or time[1] < '4' else '1')
        # sb.append(time[1] if time[1] != '?' else '3' if sb[0] == '2' else '9')
        # sb.append(':')
        # sb.append('5' if time[3] == '?' else time[3])
        # sb.append('9' if time[4] == '?' else time[4])
        # return ''.join(sb)

        # 2. 贪心
        time = list(time)
        if time[0] == '?':
            time[0] = '2' if time[1] in ('0', '1', '2', '3', '?') else '1'
        if time[1] == '?':
            time[1] = '9' if time[0] in ('0', '1') else '3'
        if time[3] == '?':
            time[3] = '5'
        if time[4] == '?':
            time[4] = '9'
        return "".join(time)
        # 复杂度分析
        # 时间复杂度：O(1)。
        # 空间复杂度：O(1)。


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ("2?:?0", "23:50"),
        ("0?:3?", "09:39"),
        ("1?:22", "19:22"),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.maximumTime(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)

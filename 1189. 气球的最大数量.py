# -*- encoding: utf-8 -*-
'''
@File    :   1189. “气球” 的最大数量.py
@Time    :   2022/02/13 21:16:41
@Author  :   henfy
@Diffi   :   Easy
@Version :   1.0

题目：https://leetcode-cn.com/problems/maximum-number-of-balloons/
'''


from typing import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        word = 'ballon'
        dict = {'l': 0, 'o': 0, 'n': 0, 'b': 0, 'a': 0}
        for x in text:
            if x in word:
                # print('x', x)
                if x in dict:
                    dict[x] += 1
        dict['l'] //= 2
        dict['o'] //= 2
        # print(dict)
        # print(min(dict))
        xiao = dict['l']
        for x in dict:
            # print(x)
            xiao = min(xiao, dict[x])
        # print(dict[min(dict)])
        # print(xiao)
        return xiao

        # cnt = Counter(ch for ch in text if ch in "balon")
        # print(cnt)
        # cnt['l'] //= 2
        # cnt['o'] //= 2
        # return min(cnt.values()) if len(cnt) == 5 else 0


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ("nlaebolko", 1),
        ("loonbalxballpoon", 2),
        ("leetcode", 0),
        ("ballon", 0),
        ("balon", 0)
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.maxNumberOfBalloons(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)

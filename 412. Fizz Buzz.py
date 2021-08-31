# -*- encoding: utf-8 -*-
'''
@File    :   412. Fizz Buzz.py
@Time    :   2021/08/03 23:01:06
@Author  :   henfy
@Diffi   :   Easy
@Version :   1.0

题目：https://leetcode-cn.com/problems/fizz-buzz/
'''


from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for i in range(1, n+1):
            if i % 15 == 0:
                ans.append("FizzBuzz")
            elif i % 3 == 0:
                ans.append("Fizz")
            elif i % 5 == 0:
                ans.append("Buzz")
            else:
                ans.append(str(i))
        return ans
        # 执行用时：16 ms, 在所有 Python 提交中击败了86.89%的用户
        # 内存消耗：13.8 MB, 在所有 Python 提交中击败了68.16%的用户


if __name__ == '__main__':
    s = Solution()
    test_list = [
        (3, ["1", "2", "Fizz"]),
        (5, ["1", "2", "Fizz", "4", "Buzz"]),
        (15, ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8",
         "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.fizzBuzz(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)

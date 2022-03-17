# -*- encoding: utf-8 -*-
'''
@File    :   393. UTF-8 编码验证.py
@Time    :   2022/03/13 23:30:24
@Author  :   henfy
@Diffi   :   Middle
@Version :   1.0

题目：https://leetcode-cn.com/problems/utf-8-validation/
'''


from typing import List


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        # 有点复杂
        MASK1, MASK2 = 1 << 7, (1 << 7) | (1 << 6)

        def getBytes(num: int) -> int:
            if (num & MASK1) == 0:
                return 1
            n, mask = 0, MASK1
            while num & mask:
                n += 1
                if n > 4:
                    return -1
                mask >>= 1
            return n if n >= 2 else -1

        index, m = 0, len(data)
        while index < m:
            n = getBytes(data[index])
            if n < 0 or index + n > m or any((ch & MASK2) != MASK1 for ch in data[index + 1: index + n]):
                return False
            index += n
        return True


if __name__ == '__main__':
    s = Solution()
    test_list = [
        # ([197, 130, 1], True),
        ([235, 140, 4], False)
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.validUtf8(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)

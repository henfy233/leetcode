# -*- encoding: utf-8 -*-
'''
@File    :   6. Z 字形变换.py
@Time    :   2022/03/01 12:24:19
@Author  :   henfy
@Diffi   :   Middle
@Version :   1.0

题目：https://leetcode-cn.com/problems/zigzag-conversion/
'''


from itertools import chain


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # 自己做，耗了很多时间
        if numRows == 1:
            return s
        res = [[] for _ in range(numRows)]
        # 这里竟然不会像上面这样写
        # res = [[]*numRows]
        # res = []
        # for i in range(numRows):
        #     res.append([])
        # print('res', res)
        res[0].append(s[0])
        for index, x in enumerate(s[1:]):
            i = index//(numRows-1)
            j = index % (numRows-1)
            # print('i', i, 'j', j)
            if i % 2 == 0:
                res[j+1].append(x)
            else:
                res[numRows-j-2].append(x)
            # print(res)
        # print(res)
        ans = ''
        for i in range(len(res)):
            ans += ''.join(res[i])
        # print(ans)
        return ans

        # 1.利用二维矩阵模拟
        # n, r = len(s), numRows
        # if r == 1 or r >= n:
        #     return s
        # t = r * 2 - 2
        # c = (n + t - 1) // t * (r - 1)
        # mat = [[''] * c for _ in range(r)]
        # x, y = 0, 0
        # for i, ch in enumerate(s):
        #     mat[x][y] = ch
        #     if i % t < r - 1:
        #         x += 1  # 向下移动
        #     else:
        #         x -= 1
        #         y += 1  # 向右上移动
        # return ''.join(ch for row in mat for ch in row if ch)

        # 2.压缩矩阵空间
        # r = numRows
        # if r == 1 or r >= len(s):
        #     return s
        # mat = [[] for _ in range(r)]
        # t, x = r * 2 - 2, 0
        # for i, ch in enumerate(s):
        #     mat[x].append(ch)
        #     x += 1 if i % t < r - 1 else -1
        # return ''.join(chain(*mat))

        # 3.直接构造
        # n, r = len(s), numRows
        # if r == 1 or r >= n:
        #     return s
        # t = r * 2 - 2
        # ans = []
        # for i in range(r):  # 枚举矩阵的行
        #     for j in range(0, n - i, t):  # 枚举每个周期的起始下标
        #         ans.append(s[j + i])  # 当前周期的第一个字符
        #         if 0 < i < r - 1 and j + t - i < n:
        #             ans.append(s[j + t - i])  # 当前周期的第二个字符
        # return ''.join(ans)


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),
        ("PAYPALISHIRING", 4, "PINALSIGYAHRPI"),
        ("A", 1, "A")
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.convert(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)

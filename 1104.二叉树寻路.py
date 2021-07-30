#
# @lc app=leetcode.cn id=1104 lang=python
#
# [1104] 二叉树寻路
#
import math
# @lc code=start


class Solution(object):
    def pathInZigZagTree(self, label):
        """
        :type label: int
        :rtype: List[int]
        """
        # 1. 自己写，没有用位运算，但是思路是正确的
        # sum = 0
        # row = 1
        # rowStart = 1
        # while rowStart*2 <= label:
        #     row += 1
        #     rowStart *= 2
        # d = [0]*(row+1)
        # path = []
        # for i in range(row+1):
        #     print(2**i)
        #     sum += 2**i
        #     d[i] = (sum+sum-2**i+1)
        #     # print('sum', sum)
        # # print('d', d)
        # while label:
        #     path.append(label)
        #     label //= 2
        # # print(path)
        # an = len(path)
        # for i in range(an//2):
        #     j = (2*i)+1
        #     path[j] = d[an-j-1] - path[j]
        # path.reverse()
        # return path

        # 1. 数学解决 getReverse函数为每列相反对应节点
        # def getReverse(label, row):
        #     return (1 << row - 1) + (1 << row) - 1 - label
        # row = 1
        # rowStart = 1
        # while rowStart * 2 <= label:
        #     row += 1
        #     rowStart *= 2
        # if row % 2 == 0:
        #     label = getReverse(label, row)
        # path = []
        # while row > 0:
        #     if row % 2 == 0:
        #         path.append(getReverse(label, row))
        #     else:
        #         path.append(label)
        #     row -= 1
        #     label >>= 1
        # path.reverse()
        # return path

        # 2. python最短写法 厉害
        row = int(math.log2(label))+1
        ans = [0]*row
        while row:
            ans[row-1] = label
            label = (2**row-1-label+2**(row-1))//2
            row -= 1
        return ans

        # @lc code=end


if __name__ == '__main__':
    s = Solution()
    test_list = [
        (14, [1, 3, 4, 14]),
        (26, [1, 2, 6, 10, 26]),
        # (215, []),
        (8, [1, 2, 7, 8]),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.pathInZigZagTree(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)

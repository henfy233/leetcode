# -*- encoding: utf-8 -*-
'''
@File    :   剑指 Offer 04. 二维数组中的查找.py
@Time    :   2022/04/25 16:34:50
@Author  :   henfy
@Diffi   :   Middle
@Version :   1.0

题目：https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof/
'''


from typing import List


class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        # 暴力法 我的想法是每行每列都进行二分法来找，但感觉这种方法不是最优的
        # if len(matrix) == 0:
        #     return False
        # n, m = len(matrix), len(matrix[0])
        # print(n, m)
        # for i in range(n):
        #     for j in range(m):
        #         if matrix[i][j] == target:
        #             return True
        # return False
        '''
        作者：jyd
        链接：https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof/solution/mian-shi-ti-04-er-wei-shu-zu-zhong-de-cha-zhao-zuo/
        来源：力扣（LeetCode）
        著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        '''
        # 线性查找
        i, j = len(matrix)-1, 0
        while i >= 0 and j < len(matrix[0]):
            if matrix[i][j] > target:
                i -= 1
            elif matrix[i][j] < target:
                j += 1
            else:
                return True
        return False


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([
            [1,   4,  7, 11],
            [2,   5,  8, 12],
            [3,   6,  9, 16],
            [10, 13, 14, 17],
            [18, 21, 23, 26]
        ], 23, True),
        ([
            [1,   4,  7, 11, 15],
            [2,   5,  8, 12, 19],
            [3,   6,  9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30]
        ], 5, True),
        ([
            [1,   4,  7, 11, 15],
            [2,   5,  8, 12, 19],
            [3,   6,  9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30]
        ], 20, False),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.findNumberIn2DArray(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)

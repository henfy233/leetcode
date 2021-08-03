#
# @lc app=leetcode.cn id=1337 lang=python
#
# [1337] 矩阵中战斗力最弱的 K 行
#

# @lc code=start
class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        # 自己写，两数组用来处理
        # res, ans = [], []
        # for i in range(len(mat)):
        #     sum = 0
        #     for j in range(len(mat[0])):
        #         if mat[i][j] != 1:
        #             break
        #         sum += 1
        #     # print('sum', sum)
        #     res.append([sum, i])
        # # print('res', res)
        # res.sort()
        # # print('res.sort', res)
        # for i in range(k):
        #     ans.append(res[i][1])
        # return ans
        # 执行用时：28 ms, 在所有 Python 提交中击败了35.48 % 的用户
        # 内存消耗：13 MB, 在所有 Python 提交中击败了93.55 % 的用户

        # 1. 二分查找 + 堆
        import heapq
        m, n = len(mat), len(mat[0])
        power = list()
        for i in range(m):
            l, r, pos = 0, n - 1, -1
            while l <= r:
                mid = (l + r) // 2
                if mat[i][mid] == 0:
                    r = mid - 1
                else:
                    pos = mid
                    l = mid + 1
            power.append((pos + 1, i))
        heapq.heapify(power)
        ans = list()
        for i in range(k):
            ans.append(heapq.heappop(power)[1])
        return ans
        # 执行用时：20 ms, 在所有 Python 提交中击败了82.26 % 的用户
        # 内存消耗：13.3 MB, 在所有 Python 提交中击败了24.19 % 的用户

        # 2. 二分查找 + 快速选择


# @lc code=end


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([[1, 1, 0, 0, 0],
          [1, 1, 1, 1, 0],
            [1, 0, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [1, 1, 1, 1, 1]], 3, [2, 0, 3]),
        ([[1, 0, 0, 0],
          [1, 1, 1, 1],
          [1, 0, 0, 0],
          [1, 0, 0, 0]], 2, [0, 2]),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.kWeakestRows(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)

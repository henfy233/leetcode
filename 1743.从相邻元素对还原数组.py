#
# @lc app=leetcode.cn id=1743 lang=python
#
# [1743] 从相邻元素对还原数组
#

# @lc code=start
class Solution(object):
    def restoreArray(self, adjacentPairs):
        """
        :type adjacentPairs: List[List[int]]
        :rtype: List[int]
        """
        res = {}
        for a, b in adjacentPairs:
            if res.get(a):
                if res.get(b):
                    m, n = res[a][-1], res[b][-1]
                    res[m] = res[a][::-1]+res[b]
                    res[n] = res[m][::-1]
                    del res[a], res[b]
                else:
                    res[res[a][-1]].append(b)
                    res[a].insert(0, b)
                    res[b] = res[a]
                    del res[a]
            else:
                if res.get(b):
                    res[res[b][-1]].append(a)
                    res[b].insert(0, a)
                    res[a] = res[b]
                    del res[b]
                else:
                    res[a] = [a, b]
                    res[b] = [b, a]
        return res[list(res.keys())[0]]

# @lc code=end


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([[2, 1], [3, 4], [3, 2]], [1, 2, 3, 4]),
        ([[4, -2], [1, 4], [-3, 1]], [-2, 4, 1, -3]),
        ([[100000, -100000]], [100000, -100000]),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.restoreArray(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)

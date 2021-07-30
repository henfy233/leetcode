#
# @lc app=leetcode.cn id=171 lang=python
#
# [171] Excel表列序号
#

# @lc code=start
class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        sum = 0
        for i in columnTitle:
            sum = sum*26 + ord(i)-64
        return sum
# @lc code=end


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ("A", 1),
        ("AB", 28),
        ("ZY", 701),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.titleToNumber(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)

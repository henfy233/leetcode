# -*- encoding: utf-8 -*-
'''
@File    :   388. 文件的最长绝对路径.py
@Time    :   2022/04/20 00:21:23
@Author  :   henfy
@Diffi   :   Middle
@Version :   1.0

题目：https://leetcode-cn.com/problems/longest-absolute-file-path/
'''


class Solution:
    def lengthLongestPath(self, input: str) -> int:
        # 栈, 不会
        st = []
        ans, i, n = 0, 0, len(input)
        while i < n:
            # 检测当前文件的深度
            depth = 1
            while i < n and input[i] == '\t':
                depth += 1
                i += 1

            # 统计当前文件名的长度
            length, isFile = 0, False
            while i < n and input[i] != '\n':
                if input[i] == '.':
                    isFile = True
                length += 1
                i += 1
            i += 1

            while len(st) >= depth:
                st.pop()
            if st:
                length += st[-1]+1
            if isFile:
                ans = max(ans, length)
            else:
                st.append(length)
        return ans


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext", 20),
        ("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext", 32)
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.lengthLongestPath(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)

#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   二叉树的最大深度.py
@Time    :   2021/07/28 16:27:09
@Author  :   henfy
@Version :   1.0
'''

# here put the import lib


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1

        # 自己写 数组元素用全局
        # maxDepth = [0]
        # def dfs(node, depth):
        #     if not node:
        #         return
        #     print('val', node.val)
        #     print('depth', depth)
        #     if depth > maxDepth[0]:
        #         maxDepth[0] = depth
        #     dfs(node.left, depth+1)
        #     dfs(node.right, depth+1)
        # dfs(root, 1)
        # return maxDepth[0]

        # python 1行代码
        # return 0 if not root else max(self.maxDepth(root.left), self.maxDepth(root.right))+1


if __name__ == '__main__':
    s = Solution()
    test_list = [
        (),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.maxDepth(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)

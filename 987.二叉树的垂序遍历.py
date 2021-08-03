#
# @lc app=leetcode.cn id=987 lang=python
#
# [987] 二叉树的垂序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # 自己写，时间慢
        # n = 1
        # tmp = root
        # l = []
        # # while tmp:
        # #     tmp = tmp.left
        # #     n+=1
        # maxDepth = [0]

        # def dfs_depth(node, depth):
        #     if not node:
        #         return
        #     print('val', node.val)
        #     print('depth', depth)
        #     if depth > maxDepth[0]:
        #         maxDepth[0] = depth
        #     dfs_depth(node.left, depth+1)
        #     dfs_depth(node.right, depth+1)
        # dfs_depth(root, 1)
        # n = maxDepth[0]
        # # print(n)
        # total = n*2+1
        # res = [[-1]*total for _ in range(n+1)]
        # # print(len(res[2]))

        # def dfs(root, x, y):
        #     if not root:
        #         return
        #     print('x', x, 'y', y)
        #     if res[x][y] != -1:
        #         print('res[x][y]', res[x][y])
        #         res[x][y].append(root.val)
        #         res[x][y].sort()
        #     else:
        #         res[x][y] = [root.val]
        #     print('res', res)
        #     dfs(root.left, x+1, y-1)
        #     dfs(root.right, x+1, y+1)
        # dfs(root, 0, n)
        # # print('total',total)
        # # print('n',n+1)
        # for i in range(total):
        #     tmp = []
        #     for j in range(n+1):
        #         if res[j][i] != -1:
        #             # tmp.append(res[j][i])
        #             tmp += res[j][i]
        #     if tmp != []:
        #         print('tmp', tmp)
        #         l.append(tmp)
        # return l

        # 自定义排序 题解 可以这样定义数组形式
        nodes = []

        def dfs(node, row, col):
            if not node:
                return
            nodes.append((col, row, node.val))
            dfs(node.left, row + 1, col - 1)
            dfs(node.right, row + 1, col + 1)
        dfs(root, 0, 0)
        print('nodes', nodes)
        nodes.sort()
        print('nodes.sort()', nodes)
        ans, lastcol = list(), float("-inf")
        for col, row, value in nodes:
            if col != lastcol:
                lastcol = col
                ans.append(list())
            ans[-1].append(value)
            print('ans', ans)
        return ans

        # ('nodes', [(0, 0, 1), (-1, 1, 2), (-2, 2, 4),
        #  (0, 2, 6), (1, 1, 3), (0, 2, 5), (2, 2, 7)])
        # ('nodes.sort()', [(-2, 2, 4), (-1, 1, 2), (0, 0, 1),
        # (0, 2, 5), (0, 2, 6), (1, 1, 3), (2, 2, 7)])
        # ('ans', [[4]])
        # ('ans', [[4], [2]])
        # ('ans', [[4], [2], [1]])
        # ('ans', [[4], [2], [1, 5]])
        # ('ans', [[4], [2], [1, 5, 6]])
        # ('ans', [[4], [2], [1, 5, 6], [3]])
        # ('ans', [[4], [2], [1, 5, 6], [3], [7]])

# @lc code=end


if __name__ == '__main__':
    s = Solution()
    test_list = [
        (1, 1),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.verticalTraversal(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)

#
# @lc app=leetcode.cn id=671 lang=python
#
# [671] 二叉树中第二小的节点
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # python 特性
        def dfs(root):
            # print('val', root.val)
            if root == None:
                return None
            # print('left', root.left.val)
            dfs(root.left)
            dfs(root.right)
            return d.append(root.val)
        d = []
        dfs(root)
        # print(d)
        b = sorted(list(set(d)))
        # print('b', b)
        if len(b) == 1:
            return -1
        else:
            return b[1]

        # python3
        # ans, rootvalue = -1, root.val
        # def dfs(root):
        #     nonlocal ans
        #     if root == None:
        #         return
        #     if ans != -1 and root.val >= ans:
        #         return
        #     if root.val > rootvalue:
        #         ans = root.val
        #     dfs(root.left)
        #     dfs(root.right)
        # dfs(root)
        # return ans


# @lc code=end
if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([2, 2, 5, None, None, 5, 7], 5),
        ([2, 2, 2], -1)
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        # arr = test[0]
        # print('arr', arr)
        # node = TreeNode(arr[0])
        # head = node
        # while
        # for i in range(1, len(arr)):
        #     if (i+1) % 2 == 0:
        #         head.left = TreeNode(arr[i])
        #         tmp1 = node.left
        #     else:
        #         head.right = TreeNode(arr[i])
        #         tmp2 = node.right
        test_result = s.findSecondMinimumValue(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)

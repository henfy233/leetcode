#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   删除链表的倒数第N个节点.py
@Time    :   2021/08/03 15:02:58
@Author  :   henfy
@Version :   1.0
'''

# here put the import lib


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 有疑惑，需重做
class Solution(object):
    def insert(self, res):
        node = ListNode(res[0])
        tmp = node
        for i in res[1:]:
            head = ListNode(i)
            tmp.next = head
            tmp = tmp.next
        return node

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # 1.1 双指针求解
        # # 数组中有快慢指针，链表同样也可以创建快慢两个指针。 然右指针先跑N+1，然后左指针在和右指针开始同步向前
        # left = right = head
        # count = 0
        # while count < n:
        #     right = right.next
        #     count += 1
        # # 当右指针跑了N+1后，已经超出链表，那么代表链表长度与N相等
        # if not right:
        #     # 那倒数第N个数就是链表头，此时只需要返回head.next即可
        #     return head.next
        # while right.next:
        #     left = left.next
        #     right = right.next
        # # 当右指针到达末尾
        # if left.next:
        #     left.next = left.next.next
        # return head

        # 1.2 双指针求解
        # 定义哑终端，便于前项循环使用
        dummy = ListNode(0)
        dummy.next = head
        # 定义快慢指针，
        slow, fast = dummy, head
        # 先让fast跑n步
        for _ in range(n):
            fast = fast.next
        # 快慢节点同步跑，循环到fast末尾，退出
        while fast:
            fast = fast.next
            slow = slow.next
        # 将fast 连接下下一个，调过N位置
        slow.next = slow.next.next
        # 返回已经修改后的链表，dummy是哑终端，所以next才是真实链表
        return dummy.next

        # 2. 非递归解决 求长度,再 for删除索引点


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),
        ([1], 1, []),
        ([1, 2], 1, [1]),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        head, n = test
        l = s.insert(head)
        test_result = s.removeNthFromEnd(l, n)
        # while test_result:
        #     print('test_result', test_result.val)
        #     test_result = test_result.next
        result = s.insert(result)
        # while result:
        #     print('result', result.val)
        #     result = result.next
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)

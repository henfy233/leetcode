#
# @lc app=leetcode.cn id=2 lang=python
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 由于输入的两个链表都是逆序存储数字的位数的，因此两个链表中同一位置的数字可以
# 直接相加。我们同时遍历两个链表，逐位计算它们的和，并与当前位置的进位值相加。
# 具体而言，如果当前两个链表处相应位置的数字为 n1, n2，进位值为 carry，
# 则它们的和为 n1+n2+carry；其中，答案链表处相应位置的数字为
# (n1+ n2 + carry) mod 10，而新的进位值为(n1+n2 +carry)/10。
# 如果两个链表的长度不同，则可以认为长度短的链表的后面有若干个 0 。
# 此外，如果链表遍历结束后，有 carry > 0，还需要在答案链表的后面附加一个节点，
# 节点的值为 carry。


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = None
        tail = None
        carry = 0
        while l1 or l2:
            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0
            sum = n1 + n2 + carry
            if not head:
                head = tail = ListNode(sum % 10)
            else:
                tail.next = ListNode(sum % 10)
                tail = tail.next
            carry = sum/10
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry > 0:
            tail.next = ListNode(carry)
        return head
# @lc code=end

# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/2/16 19:24
"""
"""
给你单链表的头指针head和两个整数left和right，其中left<=right。请你反转从位置left到位置right的链表节点，返回反转后的链表。

输入：head = [1,2,3,4,5], left = 2, right = 4
输出：[1,4,3,2,5]

输入：head = [5], left = 1, right = 1
输出：[5]
"""
"""
思路：
（1）快指针走的时候慢的也走，然后用头插法
（2）先让快指针走left-1步，然后再走right-left步，用头插法
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    @staticmethod
    def reverse_between(head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        # temp = ListNode()
        # temp.next = head
        # head = temp
        # count_slow, count_fast = 0, 0
        # slow, fast = head, head
        # while fast.next and count_fast != right:
        #     count_fast += 1
        #     fast = fast.next
        #     if count_slow != left-1:
        #         count_slow += 1
        #         slow = slow.next
        # temp = slow.next
        # slow.next = fast.next
        # fast.next = None
        # while temp != fast:
        #     new_temp = temp.next
        #     temp.next = slow.next
        #     slow.next = temp
        #     temp = new_temp
        # temp.next = slow.next
        # slow.next = temp
        # return head.next

        dummy = ListNode()
        dummy.next = head
        pre = dummy
        for _ in range(left-1):
            pre = pre.next
        temp = pre.next
        for _ in range(right-left):
            new_temp = temp.next
            temp.next = new_temp.next
            new_temp.next = pre.next
            pre.next = new_temp
        return dummy.next

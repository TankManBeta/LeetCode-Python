# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2021/12/2 16:52
"""
"""
给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。
你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。

输入：head = [1,2,3,4]
输出：[2,1,4,3]

输入：head = []
输出：[]

输入：head = [1]
输出：[1]
"""
"""
思路：
三个指针slow、fast、temp，每次按顺序尾插fast和slow（小心循环），将slow指向temp（注意判断结束条件）
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    @staticmethod
    def swap_pairs(head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        if head.next is None:
            return head
        new_head = ListNode(-1)
        new_tail = new_head
        fast = head.next
        slow = head
        temp = head.next.next
        while slow:
            new_tail.next = fast
            new_tail = new_tail.next
            new_tail.next = slow
            new_tail = new_tail.next
            new_tail.next = None
            slow = temp
            if slow is None:
                return new_head.next
            else:
                fast = temp.next
                if fast is None:
                    new_tail.next = slow
                    return new_head.next
                else:
                    temp = fast.next

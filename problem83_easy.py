# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/2/14 21:38
"""
"""
给定一个已排序的链表的头 head ， 删除所有重复的元素，使每个元素只出现一次 。返回 已排序的链表 。

输入：head = [1,1,2]
输出：[1,2]

输入：head = [1,1,2,3,3]
输出：[1,2,3]
"""
"""
思路：当前值和下一个值相等，当前的下一个指向当前的下一个的下一个，否则当前指向当前的下一个即可
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    @staticmethod
    def delete_duplicates(head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # if not head:
        #     return head
        # slow = head
        # fast = head.next
        # while fast:
        #     while fast and slow.val == fast.val:
        #         fast = fast.next
        #     slow.next = fast
        #     if slow.next:
        #         slow = slow.next
        #         fast = slow.next
        # return head

        if not head:
            return head
        slow = head
        while slow.next:
            if slow.val == slow.next.val:
                slow.next = slow.next.next
            else:
                slow = slow.next
        return head

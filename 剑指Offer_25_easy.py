# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/5/27 17:08
"""
"""
输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。

示例1：
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
"""
"""
思路：建一个dummy_head节点，然后每次取l1和l2当中大的那个，最后上下的那个加到尾部即可
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    @staticmethod
    def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
        dummy_head = ListNode(-1)
        rear = dummy_head
        while l1 and l2:
            if l1.val <= l2.val:
                rear.next = l1
                l1 = l1.next
            else:
                rear.next = l2
                l2 = l2.next
            rear = rear.next
        if l1:
            rear.next = l1
        if l2:
            rear.next = l2
        return dummy_head.next

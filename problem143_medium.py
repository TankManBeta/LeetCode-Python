# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/3/11 11:31
"""
"""
给定一个单链表 L 的头节点 head ，单链表 L 表示为：
L0 → L1 → … → Ln - 1 → Ln
请将其重新排列后变为：
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

输入：head = [1,2,3,4]
输出：[1,4,2,3]

输入：head = [1,2,3,4,5]
输出：[1,5,2,4,3]
"""
"""
思路：首先找中间节点把链表分成两段，然后翻转后半段，然后拼接
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reorder_list(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        mid = self.middle_node(head)
        l1 = head
        l2 = mid.next
        mid.next = None
        l2 = self.reverse_list(l2)
        self.merge_list(l1, l2)

    def middle_node(self, head):
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverse_list(self, head):
        prev = None
        curr = head
        while curr:
            nextTemp = curr.next
            curr.next = prev
            prev = curr
            curr = nextTemp
        return prev

    def merge_list(self, l1, l2):
        while l1 and l2:
            l1_tmp = l1.next
            l2_tmp = l2.next
            l1.next = l2
            l1 = l1_tmp
            l2.next = l1
            l2 = l2_tmp

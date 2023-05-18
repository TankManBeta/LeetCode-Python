# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/5/17 10:12
"""
"""
定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。

示例:
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
"""
"""
思路：新建一个dummy_head，然后使用头插法即可。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    @staticmethod
    def reverseList(head: ListNode) -> ListNode:
        dummy_head = ListNode(-1)
        while head:
            tmp = head.next
            head.next = dummy_head.next
            dummy_head.next = head
            head = tmp
        return dummy_head.next

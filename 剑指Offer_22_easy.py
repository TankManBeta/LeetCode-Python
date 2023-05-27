# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/5/26 10:20
"""
"""
输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。
例如，一个链表有 6 个节点，从头节点开始，它们的值依次是 1、2、3、4、5、6。这个链表的倒数第 3 个节点是值为 4 的节点。

示例：
给定一个链表: 1->2->3->4->5, 和 k = 2.
返回链表 4->5.
"""
"""
思路：双指针，一个先走k-1步，然后两个一起走。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    @staticmethod
    def getKthFromEnd(head: ListNode, k: int) -> ListNode:
        head1 = head
        head2 = head
        for _ in range(k - 1):
            head2 = head2.next
        while head2.next:
            head1 = head1.next
            head2 = head2.next
        return head1

# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/5/26 10:47
"""
"""
给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点。
返回删除后的链表的头节点。
注意：此题对比原题有改动

示例 1:
输入: head = [4,5,1,9], val = 5
输出: [4,1,9]
解释: 给定你链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.

示例 2:
输入: head = [4,5,1,9], val = 1
输出: [4,5,9]
解释: 给定你链表中值为 1 的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -> 5 -> 9.
"""
"""
思路：用一个pre指针，然后直接遍历即可，注意空和头节点的值就是val的情况的特判
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    @staticmethod
    def deleteNode(head: ListNode, val: int) -> ListNode:
        if not head:
            return None
        if head.val == val:
            return head.next
        head1 = head.next
        pre = head
        while head1:
            if head1.val == val:
                pre.next = head1.next
                break
            head1 = head1.next
            pre = pre.next
        return head

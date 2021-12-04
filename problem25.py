# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2021/12/2 18:44
"""
"""
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
k 是一个正整数，它的值小于或等于链表的长度。
如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

进阶：
你可以设计一个只使用常数额外空间的算法来解决此问题吗？
你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
 
输入：head = [1,2,3,4,5], k = 2
输出：[2,1,4,3,5]

输入：head = [1,2,3,4,5], k = 3
输出：[3,2,1,4,5]

输入：head = [1,2,3,4,5], k = 1
输出：[1,2,3,4,5]

输入：head = [1], k = 1
输出：[1]
"""
"""
思路：
每次取k个翻转，再进行拼接
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    @staticmethod
    def reverse_k_group(head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        def reverse_linklist(head1):
            if head1 is None:
                return None
            if head1.next is None:
                return head1
            new_head1 = ListNode(-1)
            while head1:
                temp = head1.next
                head1.next = new_head1.next
                new_head1.next = head1
                head1 = temp
            return new_head1.next

        new_head = ListNode(-1)
        new_head.next = head
        tail = new_head
        pre = new_head
        while tail.next:
            # 获取需要翻转的列表
            i = 0
            while i < k and tail:
                tail = tail.next
                i += 1
            if not tail:
                break
            start_node = pre.next
            next_node = tail.next
            tail.next = None

            pre.next = reverse_linklist(start_node)

            start_node.next = next_node

            pre = start_node
            tail = pre
        return new_head.next

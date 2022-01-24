# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/1/24 11:47
"""
"""
给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置。

输入：head = [1,2,3,4,5], k = 2
输出：[4,5,1,2,3]

输入：head = [0,1,2], k = 4
输出：[2,0,1]
"""
"""
思路：首先统计链表长度，可以看出当k>n（链表长度）时，旋转的个数为(k%n)，然后用快慢指针即可，慢指针的下一个就是新的头，
快指针的下一个指向原来的头。
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    @staticmethod
    def rotate_right(head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        count = 0
        temp = head
        while temp is not None:
            count += 1
            temp = temp.next
        if count == 0:
            return head
        new_k = k % count
        if new_k == 0:
            return head
        temp, fast, slow = head, head, head
        for _ in range(new_k):
            fast = fast.next
        while fast.next is not None:
            fast = fast.next
            slow = slow.next
        new_head = slow.next
        slow.next = None
        fast.next = head
        return new_head

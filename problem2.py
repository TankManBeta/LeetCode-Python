# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2021/10/27 22:13
"""
"""
给你两个非空的链表，表示两个非负的整数。它们每位数字都是按照逆序的方式存储的，并且每个节点只能存储一位数字。
请你将两个数相加，并以相同形式返回一个表示和的链表。
你可以假设除了数字0之外，这两个数都不会以0开头。

输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.

输入：l1 = [0], l2 = [0]
输出：[0]

输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
输出：[8,9,9,9,0,0,0,1]
"""
"""
思路：先将数还原，再做加法，最后表示
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    @staticmethod
    def add_two_numbers(l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = 0
        num2 = 0
        count1 = 0
        count2 = 0
        while l1 is not None:
            num1 += (10 ** count1) * l1.val
            count1 += 1
            l1 = l1.next
        while l2 is not None:
            num2 += (10 ** count2) * l2.val
            count2 += 1
            l2 = l2.next
        sum_list = list(str(num1 + num2))
        sum_list.reverse()
        first_node = ListNode(int(sum_list[0]))
        result_node = first_node
        for i in range(1, len(sum_list)):
            temp_node = ListNode(int(sum_list[i]))
            first_node.next = temp_node
            first_node = first_node.next
        return result_node

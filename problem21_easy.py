# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2021/12/2 14:45
"""
"""
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]

输入：l1 = [], l2 = []
输出：[]

输入：l1 = [], l2 = [0]
输出：[0]
"""
"""
思路：
直接哪个小放哪个
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    @staticmethod
    def merge_two_lists(list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1 is None and list2 is None:
            return None
        head = ListNode(-1)
        aux_node = head
        while list1 and list2:
            if list1.val <= list2.val:
                aux_node.next = list1
                list1 = list1.next
            else:
                aux_node.next = list2
                list2 = list2.next
            aux_node = aux_node.next
        aux_node.next = list1 if list1 is not None else list2
        return head.next

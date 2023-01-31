# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/1/30 10:03
"""
"""
给你两个链表 list1 和 list2 ，它们包含的元素分别为 n 个和 m 个。
请你将 list1 中下标从 a 到 b 的全部节点都删除，并将list2 接在被删除节点的位置。
请你返回结果链表的头指针。 

示例 1：
输入：list1 = [0,1,2,3,4,5], a = 3, b = 4, list2 = [1000000,1000001,1000002]
输出：[0,1,2,1000000,1000001,1000002,5]
解释：我们删除 list1 中下标为 3 和 4 的两个节点，并将 list2 接在该位置。上图中蓝色的边和节点为答案链表。

示例 2：
输入：list1 = [0,1,2,3,4,5,6], a = 2, b = 5, list2 = [1000000,1000001,1000002,1000003,1000004]
输出：[0,1,1000000,1000001,1000002,1000003,1000004,6]
解释：上图中蓝色的边和节点为答案链表。
"""
"""
思路：找到要拼接的节点，然后接上即可
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def mergeInBetween(list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        head1 = list1
        tail1 = list1
        for _ in range(a - 1):
            head1 = head1.next
        for _ in range(b + 1):
            tail1 = tail1.next
        head2 = list2
        tail2 = list2
        while tail2.next:
            tail2 = tail2.next
        head1.next = head2
        tail2.next = tail1
        return list1

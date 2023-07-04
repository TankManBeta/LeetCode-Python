# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/7/3 21:25
"""
from typing import Optional

"""
给你两个 非空 链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。
你可以假设除了数字 0 之外，这两个数字都不会以零开头。

示例1：
输入：l1 = [7,2,4,3], l2 = [5,6,4]
输出：[7,8,0,7]

示例2：
输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[8,0,7]

示例3：
输入：l1 = [0], l2 = [0]
输出：[0]
"""
"""
思路：我们可以使用两个栈 s1 和 s2 分别存储两个链表元素，然后同时遍历两个栈，并使用变量 carry 表示当前是否有进位。遍历时，我们
弹出对应栈的栈顶元素，计算它们与进位 carry 的和，然后更新进位的值，并创建一个链表节点，插入答案链表的头部。如果两个栈都遍历结束，
并且进位为 0 时，遍历结束。最后我们返回答案链表的头节点即可。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1, s2 = [], []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        dummy = ListNode()
        carry = 0
        while s1 or s2 or carry:
            s = (0 if not s1 else s1.pop()) + (0 if not s2 else s2.pop()) + carry
            carry, val = divmod(s, 10)
            dummy.next = ListNode(val, dummy.next)
        return dummy.next

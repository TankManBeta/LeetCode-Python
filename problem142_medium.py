# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/3/11 11:16
"""
"""
给定一个链表的头节点  head ，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 
为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。
不允许修改 链表。

输入：head = [3,2,0,-4], pos = 1
输出：返回索引为 1 的链表节点
解释：链表中有一个环，其尾部连接到第二个节点。

输入：head = [1,2], pos = 0
输出：返回索引为 0 的链表节点
解释：链表中有一个环，其尾部连接到第一个节点。

输入：head = [1], pos = -1
输出：返回 null
解释：链表中没有环。
"""
"""
思路：快慢指针，如果快慢指针相遇的话用一个temp指向头，然后temp遇到slow的时候就是入环位置
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    @staticmethod
    def detect_cycle(head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = head
        slow = head
        while fast:
            if not fast.next:
                return None
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                temp = head
                while temp != slow:
                    slow = slow.next
                    temp = temp.next
                return temp
        return None

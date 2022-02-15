# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/2/15 17:24
"""
"""
给你一个链表的头节点 head 和一个特定值 x ，请你对链表进行分隔，使得所有 小于 x 的节点都出现在 大于或等于 x 的节点之前。
你应当 保留 两个分区中每个节点的初始相对位置。

输入：head = [1,4,3,2,5,2], x = 3
输出：[1,2,2,4,3,5]

输入：head = [2,1], x = 2
输出：[1,2]
"""
"""
思路：
（1）一直往前找，找到值>=x的前驱，把它后面那个节点移过来即可
（2）维护两个链表，一个小于x的，一个大于等于x的，然后把两个连起来即可
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    @staticmethod
    def partition(head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        # temp = ListNode()
        # a = temp
        # temp.next = head
        # while temp.next:
        #     if temp.next.val < x:
        #         temp = temp.next
        #     else:
        #         new_temp = temp
        #         while new_temp.next and new_temp.next.val >= x:
        #             new_temp = new_temp.next
        #         if new_temp.next:
        #             temp_node = ListNode(new_temp.next.val)
        #             new_temp.next = new_temp.next.next
        #             temp_node.next = temp.next
        #             temp.next = temp_node
        #             temp = temp.next
        #         else:
        #             break
        # return a.next

        head1, head2 = ListNode(), ListNode()
        tail1, tail2 = head1, head2
        while head:
            if head.val < x:
                temp = ListNode(head.val)
                tail1.next = temp
                tail1 = tail1.next
            else:
                temp = ListNode(head.val)
                tail2.next = temp
                tail2 = tail2.next
            head = head.next
        tail1.next = head2.next
        return head1.next

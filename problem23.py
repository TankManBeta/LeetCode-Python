# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2021/12/2 16:21
"""
"""
给你一个链表数组，每个链表都已经按升序排列。
请你将所有链表合并到一个升序链表中，返回合并后的链表。

输入：lists = [[1,4,5],[1,3,4],[2,6]]
输出：[1,1,2,3,4,4,5,6]
解释：链表数组如下：
[1->4->5, 1->3->4, 2->6]
将它们合并到一个有序链表中得到。
1->1->2->3->4->4->5->6

输入：lists = []
输出：[]

输入：lists = [[]]
输出：[]
"""
"""
思路：同合并两个升序链表思路相同
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    @staticmethod
    def merge_k_lists(lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
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

        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]

        ans = None
        for i in lists:
            ans = merge_two_lists(ans, i)
        return ans
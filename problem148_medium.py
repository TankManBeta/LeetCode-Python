# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/3/14 10:39
"""
"""
给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。

输入：head = [4,2,1,3]
输出：[1,2,3,4]

输入：head = [-1,5,3,4,0]
输出：[-1,0,3,4,5]

输入：head = []
输出：[]
"""
"""
思路：
（1）找到链表一分为二，然后把两个链表分别排序，再合并排序后的链表
（2）自底向上归并排序，先让一个一个都有序，然后两两合并，然后四个四个，以此类推
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    @staticmethod
    def sort_list(head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # def sortFunc(head, tail):
        #     if not head:
        #         return head
        #     if head.next == tail:
        #         head.next = None
        #         return head
        #     slow = fast = head
        #     while fast != tail:
        #         slow = slow.next
        #         fast = fast.next
        #         if fast != tail:
        #             fast = fast.next
        #     mid = slow
        #     return merge(sortFunc(head, mid), sortFunc(mid, tail))

        # def merge(head1, head2):
        #     dummyHead = ListNode(0)
        #     temp, temp1, temp2 = dummyHead, head1, head2
        #     while temp1 and temp2:
        #         if temp1.val <= temp2.val:
        #             temp.next = temp1
        #             temp1 = temp1.next
        #         else:
        #             temp.next = temp2
        #             temp2 = temp2.next
        #         temp = temp.next
        #     if temp1:
        #         temp.next = temp1
        #     elif temp2:
        #         temp.next = temp2
        #     return dummyHead.next

        # return sortFunc(head, None)

        def merge(head1, head2):
            dummy_head = ListNode(0)
            temp, temp1, temp2 = dummy_head, head1, head2
            while temp1 and temp2:
                if temp1.val <= temp2.val:
                    temp.next = temp1
                    temp1 = temp1.next
                else:
                    temp.next = temp2
                    temp2 = temp2.next
                temp = temp.next
            if temp1:
                temp.next = temp1
            elif temp2:
                temp.next = temp2
            return dummy_head.next

        if not head:
            return head

        length = 0
        node = head
        while node:
            length += 1
            node = node.next

        dummyHead = ListNode(0, head)
        subLength = 1

        while subLength < length:
            prev, curr = dummyHead, dummyHead.next
            while curr:
                head1 = curr
                for i in range(1, subLength):
                    if curr.next:
                        curr = curr.next
                    else:
                        break
                head2 = curr.next
                curr.next = None
                curr = head2
                for i in range(1, subLength):
                    if curr and curr.next:
                        curr = curr.next
                    else:
                        break
                succ = None
                if curr:
                    succ = curr.next
                    curr.next = None
                merged = merge(head1, head2)
                prev.next = merged
                while prev.next:
                    prev = prev.next
                curr = succ
            subLength <<= 1

        return dummyHead.next

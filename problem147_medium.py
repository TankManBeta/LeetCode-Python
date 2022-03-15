# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/3/14 10:24
"""
"""
给定单个链表的头 head ，使用 插入排序 对链表进行排序，并返回 排序后链表的头 。
插入排序 算法的步骤:
    插入排序是迭代的，每次只移动一个元素，直到所有元素可以形成一个有序的输出列表。
    每次迭代中，插入排序只从输入数据中移除一个待排序的元素，找到它在序列中适当的位置，并将其插入。
    重复直到所有输入数据插入完为止。
下面是插入排序算法的一个图形示例。部分排序的列表(黑色)最初只包含列表中的第一个元素。每次迭代时，从输入数据中删除一个元素(红色)，
并就地插入已排序的列表中。
对链表进行插入排序。

输入: head = [4,2,1,3]
输出: [1,2,3,4]

输入: head = [-1,5,3,4,0]
输出: [-1,0,3,4,5]
"""
"""
思路：创建一个虚拟头节点，然后用快慢指针，初始都指向虚拟的头节点，然后看当前的temp的和fast比，如果temp比fast大就继续往后找，
否则直接停止，这时候比较temp和fast的值的大小，如果fast比temp大，说明肯定是在中间停的；否则说明是遍历到了末尾，然后插入即可
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    @staticmethod
    def insertion_sort_list(head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        dummy_head = ListNode(-5001)
        dummy_head.next = head
        tail = head
        temp = tail.next
        while temp:
            tail.next = temp.next
            fast, slow = dummy_head, dummy_head
            while fast != tail:
                if temp.val > fast.val:
                    slow = fast
                    fast = fast.next
                else:
                    break
            if temp.val > fast.val:
                fast.next = temp
                tail = temp
            else:
                temp.next = slow.next
                slow.next = temp
            temp = tail.next
        return dummy_head.next

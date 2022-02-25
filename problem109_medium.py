# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/2/24 16:36
"""
"""
给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。
本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

给定的有序链表： [-10, -3, 0, 5, 9]
一个可能的答案是：[0, -3, 9, -10, null, 5]
"""
"""
思路：快慢指针每次找中间一个即可
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    @staticmethod
    def sorted_list_to_bst(head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[TreeNode]
        """

        def get_mid(left, right):
            fast = slow = left
            while fast != right and fast.next != right:
                fast = fast.next.next
                slow = slow.next
            return slow

        def build_tree(left, right):
            if left == right:
                return None
            mid = get_mid(left, right)
            root = TreeNode(mid.val)
            root.left = build_tree(left, mid)
            root.right = build_tree(mid.next, right)
            return root
        return build_tree(head, None)

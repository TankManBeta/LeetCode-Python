# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/6/11 15:52
"""
from typing import Optional

"""
给你一个链表的头节点 head，请你编写代码，反复删去链表中由 总和 值为 0 的连续节点组成的序列，直到不存在这样的序列为止。
删除完毕后，请你返回最终结果链表的头节点。
你可以返回任何满足题目要求的答案。
（注意，下面示例中的所有序列，都是对 ListNode 对象序列化的表示。）

示例 1：
输入：head = [1,2,-3,3,1]
输出：[3,1]
提示：答案 [1,2,1] 也是正确的。

示例 2：
输入：head = [1,2,3,-3,4]
输出：[1,2,4]

示例 3：
输入：head = [1,2,3,-3,-2]
输出：[1]
"""
"""
思路：哈希表+两次遍历。第一次遍历，累加前缀和，把前缀和作为键，最后出现的地方作为值；第二次遍历，累加当前前缀和，然后把cur.next
指向last[s].next，因为两个相同的前缀和之间的数字的和肯定为0。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def removeZeroSumSublists(head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        last = {}
        s, cur = 0, dummy
        while cur:
            s += cur.val
            last[s] = cur
            cur = cur.next
        s, cur = 0, dummy
        while cur:
            s += cur.val
            cur.next = last[s].next
            cur = cur.next
        return dummy.next

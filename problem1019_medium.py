# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/4/10 9:55
"""
from typing import Optional, List

"""
给定一个长度为 n 的链表 head。对于列表中的每个节点，查找下一个 更大节点 的值。也就是说，对于每个节点，找到它旁边的第一个节点的值，
这个节点的值 严格大于 它的值。返回一个整数数组 answer ，其中 answer[i] 是第 i 个节点( 从1开始 )的下一个更大的节点的值。
如果第 i 个节点没有下一个更大的节点，设置 answer[i] = 0 。 

示例 1：
输入：head = [2,1,5]
输出：[5,5,0]

示例 2：
输入：head = [2,7,4,3,5]
输出：[7,0,5,5,0]
"""
"""
思路：
（1）直接模拟，超时
（2）单调栈，首先将所有数值存入nums中，然后维护一个单调栈stk，从后往前遍历nums，如果stk不为空并且stk[-1]≤num[i]，说明当前栈顶
肯定不可能时nums[i]右边更大的。如果此时stk为空，说明当前元素没有下一个更大的数，ans[i]=0；否则，当前元素的下一个最大元素就是
栈顶元素，更新ans，并把nums[i]放入栈中。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def nextLargerNodes(head: Optional[ListNode]) -> List[int]:
        # temp = head
        # n = 0
        # while temp:
        #     n += 1
        #     temp = temp.next
        # dummy_head = head
        # ans = [0] * n
        # i = 0
        # while dummy_head:
        #     tmp = dummy_head
        #     while tmp:
        #         if tmp.val > dummy_head.val:
        #             ans[i] = tmp.val
        #             break
        #         else:
        #             tmp = tmp.next
        #     dummy_head = dummy_head.next
        #     i += 1
        # return ans

        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        n = len(nums)
        stk = []
        ans = [0] * n
        for i in range(n - 1, -1, -1):
            while stk and stk[-1] <= nums[i]:
                stk.pop()
            if stk:
                ans[i] = stk[-1]
            stk.append(nums[i])
        return ans

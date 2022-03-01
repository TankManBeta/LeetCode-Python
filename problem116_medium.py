# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/3/1 9:20
"""
"""
给定一个 完美二叉树 ，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。
初始状态下，所有 next 指针都被设置为 NULL。

输入：root = [1,2,3,4,5,6,7]
输出：[1,#,2,3,#,4,5,6,7,#]

输入：root = []
输出：[]
"""
"""
思路：
（1）层次遍历，同一层有下一个就指向
（2）由于要求常数空间复杂度，可以利用已经标好的next指针
"""


# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution(object):
    @staticmethod
    def connect(root):
        """
        :type root: Node
        :rtype: Node
        """
        # if not root:
        #     return None
        # queue = [root]
        # temp_queue = []
        # while queue:
        #     for i in range(0, len(queue)):
        #         if i+1 < len(queue):
        #             queue[i].next = queue[i+1]
        #         if queue[i].left:
        #             temp_queue.append(queue[i].left)
        #         if queue[i].right:
        #             temp_queue.append(queue[i].right)
        #     queue = temp_queue
        #     temp_queue = []
        # return root

        if not root:
            return root
        left_most = root
        while left_most.left:
            head = left_most
            while head:
                head.left.next = head.right
                if head.next:
                    head.right.next = head.next.left
                head = head.next
            left_most = left_most.left
        return root

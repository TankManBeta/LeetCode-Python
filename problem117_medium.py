# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/3/1 9:26
"""
"""
给定一个二叉树
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。
初始状态下，所有 next 指针都被设置为 NULL。

输入：root = [1,2,3,4,5,null,7]
输出：[1,#,2,3,#,4,5,7,#]
"""
"""
思路：
（1）层次遍历
（2）要求常数空间复杂度，利用已经标好的next指针，每一次遍历当前层时，同时将下一层的节点串起来，虚拟一个dummy_head，然后pre指针
向前即可
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

        head = root
        dummy_head = Node()
        while head:
            dummy_head.next = None
            pre = dummy_head
            while head:
                if head.left:
                    pre.next = head.left
                    pre = pre.next
                if head.right:
                    pre.next = head.right
                    pre = pre.next
                head = head.next
            head = dummy_head.next
        return root

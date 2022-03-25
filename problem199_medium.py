# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/3/24 10:44
"""
"""
给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

输入: [1,2,3,null,5,null,4]
输出: [1,3,4]

输入: [1,null,3]
输出: [1,3]

输入: []
输出: []
"""
"""
思路：
（1）先序递归，同时用用哈希表记录每一层的值，同一层的右子树的值肯定覆盖左子树
（2）层次遍历，放每一层最后一个节点的值即可
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self):
        self.res_dict = {}

    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def pre_order(head, layer):
            if not head:
                return
            self.res_dict[layer] = head.val
            pre_order(head.left, layer+1)
            pre_order(head.right, layer+1)

        pre_order(root, 0)
        key_list = sorted(self.res_dict.keys())
        return [self.res_dict[i] for i in key_list]

        # res = []
        # if not root:
        #     return res
        # queue = [root]
        # while queue:
        #     temp_len = len(queue)
        #     for i in range(temp_len):
        #         temp_node = queue.pop(0)
        #         if i == temp_len - 1:
        #             res.append(temp_node.val)
        #         if temp_node.left:
        #             queue.append(temp_node.left)
        #         if temp_node.right:
        #             queue.append(temp_node.right)
        # return res

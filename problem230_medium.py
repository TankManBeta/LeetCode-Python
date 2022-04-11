# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/4/10 12:53
"""
"""
给定一个二叉搜索树的根节点 root ，和一个整数 k ，请你设计一个算法查找其中第 k 个最小元素（从 1 开始计数）。

输入：root = [3,1,4,null,2], k = 1
输出：1

输入：root = [5,3,6,2,4,null,null,1], k = 3
输出：3
"""
"""
思路：
（1）中序遍历是个升序序列，直接返回k-1
（2）可以记录下以每个结点为根结点的子树的结点数，如果node 的左子树的结点数left小于k−1，则第k小的元素一定在node的右子树中，
令node等于其的右子结点，k等于k−left−1，并继续搜索
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# class Solution(object):
#     def kthSmallest(self, root, k):
#         """
#         :type root: TreeNode
#         :type k: int
#         :rtype: int
#         """
#         self.ans = []

#         def pre_order(head):
#             if not head:
#                 return
#             pre_order(head.left)
#             self.ans.append(head.val)
#             pre_order(head.right)

#         pre_order(root)
#         return self.ans[k-1]

class MyBst:
    def __init__(self, root):
        self.root = root
        # 统计以每个结点为根结点的子树的结点数，并存储在哈希表中
        self._node_num = {}
        self._count_node_num(root)

    def kth_smallest(self, k):
        """返回二叉搜索树中第k小的元素"""
        node = self.root
        while node:
            left = self._get_node_num(node.left)
            if left < k - 1:
                node = node.right
                k -= left + 1
            elif left == k - 1:
                return node.val
            else:
                node = node.left

    def _count_node_num(self, node):
        """统计以node为根结点的子树的结点数"""
        if not node:
            return 0
        self._node_num[node] = 1 + self._count_node_num(node.left) + self._count_node_num(node.right)
        return self._node_num[node]

    def _get_node_num(self, node):
        """获取以node为根结点的子树的结点数"""
        return self._node_num[node] if node is not None else 0


class Solution:
    @staticmethod
    def kthSmallest(root, k):
        bst = MyBst(root)
        return bst.kth_smallest(k)

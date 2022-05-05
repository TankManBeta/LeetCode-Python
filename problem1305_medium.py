# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/5/1 13:39
"""
"""
给你 root1 和 root2 这两棵二叉搜索树。请你返回一个列表，其中包含 两棵树 中的所有整数并按 升序 排序。

输入：root1 = [2,1,4], root2 = [1,0,3]
输出：[0,1,1,2,3,4]

输入：root1 = [1,null,8], root2 = [8,1]
输出：[1,1,8,8]
"""
"""
思路：中序遍历这两棵二叉搜索树，可以得到两个有序数组。然后可以使用双指针方法来合并这两个有序数组，
这一方法将两个数组看作两个队列，每次从队列头部取出比较小的数字放到结果中（头部相同时可任取一个）。
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    @staticmethod
    def getAllElements(root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        def inorder(node, res):
            if node:
                inorder(node.left, res)
                res.append(node.val)
                inorder(node.right, res)

        nums1, nums2 = [], []
        inorder(root1, nums1)
        inorder(root2, nums2)

        merged = []
        p1, n1 = 0, len(nums1)
        p2, n2 = 0, len(nums2)
        while True:
            if p1 == n1:
                merged.extend(nums2[p2:])
                break
            if p2 == n2:
                merged.extend(nums1[p1:])
                break
            if nums1[p1] < nums2[p2]:
                merged.append(nums1[p1])
                p1 += 1
            else:
                merged.append(nums2[p2])
                p2 += 1
        return merged

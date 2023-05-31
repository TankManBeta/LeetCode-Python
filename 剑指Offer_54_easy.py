# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/5/30 9:33
"""
"""
给定一棵二叉搜索树，请找出其中第 k 大的节点的值。

示例 1:
输入: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
输出: 4

示例 2:
输入: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
输出: 4
"""
"""
思路：
（1）二叉搜索树的中序遍历是一个升序序列，然后取倒数第k个即可。
（2）先右子树，然后根，然后左子树，得到的是降序序列，这样可以在找到第k个就停止。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.k = 0
        self.ans = -1

    def kthLargest(self, root: TreeNode, k: int) -> int:
        # ans = []

        # def dfs(head):
        #     if not head:
        #         return
        #     dfs(head.left)
        #     ans.append(head.val)
        #     dfs(head.right)

        # dfs(root)
        # return ans[-k]

        def dfs(head):
            if not head:
                return
            dfs(head.right)
            nonlocal k
            if self.k == k:
                return
            self.k += 1
            if self.k == k:
                self.ans = head.val
            dfs(head.left)

        dfs(root)
        return self.ans

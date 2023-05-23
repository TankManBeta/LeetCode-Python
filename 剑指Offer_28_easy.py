# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/5/22 10:54
"""
"""
请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。
例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
    1
   / \
  2   2
   \   \
   3    3 

示例 1：
输入：root = [1,2,2,3,4,4,3]
输出：true

示例 2：
输入：root = [1,2,2,null,3,null,3]
输出：false
"""
"""
思路：
（1）队列，每次把当前层能放的节点放进去，包括None，然后把节点的值放到列表里，最后看列表和列表的反序是否一样。
（2）递归，设置一个函数dfs(l,r)，比较l.left.val==r.right.val以及l.right.val==r.left.val
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    @staticmethod
    def isSymmetric(root: TreeNode) -> bool:
        # if not root:
        #     return True
        # queue = [root]
        # while queue:
        #     tmp = []
        #     for i in range(len(queue)):
        #         node = queue.pop(0)
        #         if not node:
        #             tmp.append(-inf)
        #         else:
        #             tmp.append(node.val)
        #             queue.append(node.left)
        #             queue.append(node.right)
        #     if tmp != tmp[::-1]:
        #         return False
        # return True

        def recur(L, R):
            if not L and not R:
                return True
            if not L or not R or L.val != R.val:
                return False
            return recur(L.left, R.right) and recur(L.right, R.left)

        return recur(root.left, root.right) if root else True

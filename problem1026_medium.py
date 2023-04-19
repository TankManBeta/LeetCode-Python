# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/4/18 19:22
"""
from math import inf
from typing import Optional

"""
给定二叉树的根节点 root，找出存在于 不同 节点 A 和 B 之间的最大值 V，其中 V = |A.val - B.val|，且 A 是 B 的祖先。
（如果 A 的任何子节点之一为 B，或者 A 的任何子节点是 B 的祖先，那么我们认为 A 是 B 的祖先） 

示例 1：
输入：root = [8,3,10,1,6,null,14,null,null,4,7,13]
输出：7
解释： 
我们有大量的节点与其祖先的差值，其中一些如下：
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
在所有可能的差值中，最大值 7 由 |8 - 1| = 7 得出。

示例 2：
输入：root = [1,null,2,null,0,3]
输出：3
"""
"""
思路：
（1）自顶向下，每向下递归一层同时传祖先的最大值和最小值，同时更新ans
（2）自底向上，先递归到最深，然后向上传子孙的最大值和最小值，同时更新ans
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def maxAncestorDiff(root: Optional[TreeNode]) -> int:
        # def dfs(root, min_pre, max_pre):
        #     if not root:
        #         return
        #     nonlocal ans
        #     ans = max(ans, abs(min_pre-root.val), abs(max_pre-root.val))
        #     min_pre = min(min_pre, root.val)
        #     max_pre = max(max_pre, root.val)
        #     dfs(root.left, min_pre, max_pre)
        #     dfs(root.right, min_pre, max_pre)

        # ans = 0
        # dfs(root, root.val, root.val)
        # return ans

        def dfs(head):
            if not head:
                return inf, -inf
            min_des = max_des = head.val
            l_min_des, l_max_des = dfs(head.left)
            r_min_des, r_max_des = dfs(head.right)
            min_des = min(min_des, l_min_des, r_min_des)
            max_des = max(max_des, l_max_des, r_max_des)
            nonlocal ans
            ans = max(ans, max_des - head.val, head.val - min_des)
            return min_des, max_des

        ans = 0
        dfs(root)
        return ans

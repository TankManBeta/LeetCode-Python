# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/9/6 20:15
"""
from typing import Optional

"""
给你一个有根节点 root 的二叉树，返回它 最深的叶节点的最近公共祖先 。
回想一下：
叶节点 是二叉树中没有子节点的节点
树的根节点的 深度 为 0，如果某一节点的深度为 d，那它的子节点的深度就是 d+1
如果我们假定 A 是一组节点 S 的 最近公共祖先，S 中的每个节点都在以 A 为根节点的子树中，且 A 的深度达到此条件下可能的最大值。 

示例 1：
输入：root = [3,5,1,6,2,0,8,null,null,7,4]
输出：[2,7,4]
解释：我们返回值为 2 的节点，在图中用黄色标记。
在图中用蓝色标记的是树的最深的节点。
注意，节点 6、0 和 8 也是叶节点，但是它们的深度是 2 ，而节点 7 和 4 的深度是 3 。

示例 2：
输入：root = [1]
输出：[1]
解释：根节点是树中最深的节点，它是它本身的最近公共祖先。

示例 3：
输入：root = [0,1,3,null,2]
输出：[2]
解释：树中最深的叶节点是 2 ，最近公共祖先是它自己。
"""
"""
思路：我们设计一个函数 dfs(root)，它将返回一个二元组 (l,d)，其中 l 是节点 root 的最深公共祖先，而 d 是节点 root 的深度。函数 dfs(root) 
的执行逻辑如下：如果 root 为空，则返回二元组 (None,0)；否则，我们递归调用 dfs(root.left) 和 dfs(root.right)，得到二元组 (l,d1) 和 
(r,d2)。如果 d1>d2，则 root 的最深公共祖先节点为 l，深度为 d1+1；如果 d1<d2​，则 root 的最深公共祖先节点为 r，深度为 d2+1；如果 d1=d2，
则 root 的最深公共祖先节点为 root，深度为 d1+1。我们在主函数中调用 dfs(root)，并返回其返回值的第一个元素，即可得到最深公共祖先节点。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def lcaDeepestLeaves(root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root):
            if root is None:
                return None, 0
            l, d1 = dfs(root.left)
            r, d2 = dfs(root.right)
            if d1 > d2:
                return l, d1 + 1
            if d1 < d2:
                return r, d2 + 1
            return root, d1 + 1

        return dfs(root)[0]

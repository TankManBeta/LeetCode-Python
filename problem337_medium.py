# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/9/18 22:09
"""
from typing import Optional

"""
小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为 root 。
除了 root 之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果 两个直接相连
的房子在同一天晚上被打劫 ，房屋将自动报警。
给定二叉树的 root 。返回 在不触动警报的情况下 ，小偷能够盗取的最高金额 。 

示例 1:
输入: root = [3,2,3,null,3,null,1]
输出: 7 
解释: 小偷一晚能够盗取的最高金额 3 + 3 + 1 = 7

示例 2:
输入: root = [3,4,5,1,3,null,1]
输出: 9
解释: 小偷一晚能够盗取的最高金额 4 + 5 = 9
"""
"""
思路：我们定义一个函数 dfs(root)，表示偷取以 root 为根的二叉树的最大金额。该函数返回一个二元组 (a,b)，其中 a 表示偷取 root 节点时能得到的最大
金额，而 b 表示不偷取 root 节点时能得到的最大金额。
函数 dfs(root) 的计算过程如下：
如果 root 为空，那么显然有 dfs(root)=(0,0)。否则，我们首先计算出左右子节点的结果，即 dfs(root.left) 和 dfs(root.right)，这样就得到了两对值
 (la,lb) 以及 (ra,rb)。对于 dfs(root) 的结果，我们可以分为两种情况：如果偷取 root 节点，那么不能偷取其左右子节点，结果为 root.val+lb+rb ；
如果不偷取 root 节点，那么可以偷取其左右子节点，结果为 max(la,lb)+max(ra,rb)。在主函数中，我们可以直接返回 dfs(root) 的较大值，
即 max(dfs(root))。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def rob(root: Optional[TreeNode]) -> int:
        def dfs(root: Optional[TreeNode]) -> (int, int):
            if root is None:
                return 0, 0
            la, lb = dfs(root.left)
            ra, rb = dfs(root.right)
            return root.val + lb + rb, max(la, lb) + max(ra, rb)

        return max(dfs(root))

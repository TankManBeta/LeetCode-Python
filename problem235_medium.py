"""
给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。
百度百科中最近公共祖先的定义为：“对于有根树T的两个结点p、q，最近公共祖先表示为一个结点x，满足x是p、q的祖先且x的深度尽可能大
（一个节点也可以是它自己的祖先）。”
例如，给定如下二叉搜索树:root =[6,2,8,0,4,7,9,null,null,3,5]

输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
输出: 6
解释: 节点 2 和节点 8 的最近公共祖先是 6。

输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
输出: 2
解释: 节点 2 和节点 4 的最近公共祖先是 2, 因为根据定义最近公共祖先节点可以为节点本身。
"""
"""
思路：如果当前节点值大于p和q的值，说明p和q应该在当前节点的左子树上；如果当前节点的值小于p和q的值，说明p和q应该在当前节点的右子树上；如果这两种情况都
不满足，说明当前节点应该是分岔节点，不是p、q其中之一就是它们的祖先
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ancestor = root
        while True:
            if p.val < ancestor.val and q.val < ancestor.val:
                ancestor = ancestor.left
            elif p.val > ancestor.val and q.val > ancestor.val:
                ancestor = ancestor.right
            else:
                break
        return ancestor
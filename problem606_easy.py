# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/3/19 12:14
"""
"""
你需要采用前序遍历的方式，将一个二叉树转换成一个由括号和整数组成的字符串。
空节点则用一对空括号 "()" 表示。而且你需要省略所有不影响字符串与原始二叉树之间的一对一映射关系的空括号对。

输入: 二叉树: [1,2,3,4]
输出: "1(2(4))(3)"

输入: 二叉树: [1,2,3,null,4]
输出: "1(2()(4))(3)"
"""
"""
思路：dfs，如果左右节点都没有，就返回当前节点的值；如果左边有右边没有就都加括号，如果左边没有右边有就左边加括号
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    @staticmethod
    def tree2str(root):
        """
        :type root: TreeNode
        :rtype: str
        """

        def dfs(head):
            if not head:
                return ""
            if not head.left and not head.right:
                return str(head.val)
            if not head.right:
                return "{}({})".format(head.val, dfs(head.left))
            else:
                return "{}({})({})".format(head.val, dfs(head.left), dfs(head.right))

        return dfs(root)

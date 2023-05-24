# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/5/23 13:02
"""
"""
输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)
B是A的子结构， 即 A中有出现和B相同的结构和节点值。
例如:
给定的树 A:
     3
    / \
   4   5
  / \
 1   2
给定的树 B：
   4 
  /
 1
返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值。

示例 1：
输入：A = [1,2,3], B = [3,1]
输出：false

示例 2：
输入：A = [3,4,5,1,2], B = [4,1]
输出：true
"""
"""
思路：
先逐个检查a的节点，不断和b比对；如果a其中某一个节点和b第一个对上了，则挨个对比其他的子节点；
循环结束的条件是a遍历完了或者b遍历完了：
    1.a遍历完了（b没完）说明a、b对不上，返回false
    2.b遍历完了（不管a完没完），说明能对上， 返回true
    3.遍历过程中发现a、b对不上了，返回false
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    @staticmethod
    def isSubStructure(A: TreeNode, B: TreeNode) -> bool:
        if not B or not A:
            return False  # 空集直接返回

        status = False

        def dfs(node):
            if not node:
                return
            nonlocal status
            # 如果在搜索过程中，有某个节点能对上，我们跳到check函数仔细搜一搜
            if node.val == B.val:
                status = check(node, B)  # 比对结果更新到status

            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)

        def check(nA, nB):
            # 终止条件
            if not nB:
                return True
            if not nA:
                return False
            if nA.val != nB.val:
                return False

            # 不断比对，直到触发上面的终止条件
            return check(nA.left, nB.left) and check(nA.right, nB.right)

        # 执行搜索和比对
        dfs(A)

        return status

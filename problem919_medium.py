# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/2/1 18:32
"""
from collections import deque

"""
完全二叉树 是每一层（除最后一层外）都是完全填充（即，节点数达到最大）的，并且所有的节点都尽可能地集中在左侧。
设计一种算法，将一个新节点插入到一个完整的二叉树中，并在插入后保持其完整。
实现 CBTInserter 类:
    CBTInserter(TreeNode root) 使用头节点为 root 的给定树初始化该数据结构；
    CBTInserter.insert(int v)  向树中插入一个值为 Node.val == val的新节点 TreeNode。使树保持完全二叉树的状态，并返回插入节点 
    TreeNode 的父节点的值；
    CBTInserter.get_root() 将返回树的头节点。
 
示例 1：
输入
["CBTInserter", "insert", "insert", "get_root"]
[[[1, 2]], [3], [4], []]
输出
[null, 1, 2, [1, 2, 3, 4]]
解释
CBTInserter cBTInserter = new CBTInserter([1, 2]);
cBTInserter.insert(3);  // 返回 1
cBTInserter.insert(4);  // 返回 2
cBTInserter.get_root(); // 返回 [1, 2, 3, 4]
"""
"""
思路：对于一棵完全二叉树而言，其除了最后一层之外都是完全填充的，并且最后一层的节点全部在最左侧。那么，只有倒数第二层（如果存在）
最右侧的若干个节点，以及最后一层的全部节点可以再添加子节点，其余的节点都已经拥有两个子节点。因此，我们可以使用一个队列存储上述
提到的这些可以添加子节点的节点。队列中的存储顺序为：首先「从左往右」存储倒数第二层最右侧的节点，再「从左往右」存储最后一层的
全部节点。这一步可以使用广度优先搜索来完成，因为广度优先搜索就是按照层优先进行遍历的。
随后，当我们每次调用 insert(val) 时，我们就创建出一个节点 child，并将它作为队列的队首节点的子节点。在这之后，我们需要把 child 
加入队尾，并且如果对队首节点已经有两个子节点，我们需要将其从队列中移除。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class CBTInserter:

    def __init__(self, root: TreeNode):
        self.root = root
        self.candidate = deque()

        q = deque([root])
        while q:
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            if not (node.left and node.right):
                self.candidate.append(node)

    def insert(self, val: int) -> int:
        candidate_ = self.candidate

        child = TreeNode(val)
        node = candidate_[0]
        ret = node.val

        if not node.left:
            node.left = child
        else:
            node.right = child
            candidate_.popleft()

        candidate_.append(child)
        return ret

    def get_root(self) -> TreeNode:
        return self.root

# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()

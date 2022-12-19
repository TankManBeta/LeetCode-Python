# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/12/19 19:11
"""
"""
序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，
同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。
请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为
一个字符串并且将这个字符串反序列化为原始的树结构。
提示: 输入输出格式与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode 序列化二叉树的格式。
你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。

示例 1：
输入：root = [1,2,3,null,null,4,5]
输出：[1,2,3,null,null,4,5]

示例 2：
输入：root = []
输出：[]

示例 3：
输入：root = [1]
输出：[1]

示例 4：
输入：root = [1,2]
输出：[1,2]
"""
"""
思路：
（1）bfs。序列化：用BFS遍历树，与一般遍历的不同点是不管node的左右子节点是否存在，统统加到队列中；在节点出队时，如果节点不存在，
在返回值res中加入一个null；如果节点存在，则加入节点值的字符串形式。反序列化：同样使用BFS方法，利用队列新建二叉树；
首先要将data转换成列表，然后遍历，只要不为null将节点按顺序加入二叉树中；同时还要将节点入队；队列为空时遍历完毕，返回根节点。
（2）dfs。序列化：递归的第一步都是特例的处理，因为这是递归的中止条件：如果根节点为空，返回“null”；序列化的结果为：根节点值 + 
"," + 左子节点值(进入递归) + "," + 右子节点值(进入递归)；递归就是不断将“根节点”值加到结果中的过程。反序列化：先将字符串转换成队列
（python转换成列表即可），接下来就进入了递归：i.弹出左侧元素，即队列出队 ii.如果元素为“null”，返回null（python返回None）
iii.否则，新建一个值为弹出元素的新节点 iv.其左子节点为队列的下一个元素，进入递归；右子节点为队列的下下个元素，也进入递归
v.递归就是不断将子树的根节点连接到父节点的过程
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    # def serialize(self, root):
    #     """Encodes a tree to a single string.

    #     :type root: TreeNode
    #     :rtype: str
    #     """
    #     if not root:
    #         return ""
    #     queue = collections.deque([root])
    #     res = []
    #     while queue:
    #         node = queue.popleft()
    #         if node:
    #             res.append(str(node.val))
    #             queue.append(node.left)
    #             queue.append(node.right)
    #         else:
    #             res.append('None')
    #     return '[' + ','.join(res) + ']'

    # def deserialize(self, data):
    #     """Decodes your encoded data to tree.

    #     :type data: str
    #     :rtype: TreeNode
    #     """
    #     if not data:
    #         return []
    #     dataList = data[1:-1].split(',')
    #     root = TreeNode(int(dataList[0]))
    #     queue = collections.deque([root])
    #     i = 1
    #     while queue:
    #         node = queue.popleft()
    #         if dataList[i] != 'None':
    #             node.left = TreeNode(int(dataList[i]))
    #             queue.append(node.left)
    #         i += 1
    #         if dataList[i] != 'None':
    #             node.right = TreeNode(int(dataList[i]))
    #             queue.append(node.right)
    #         i += 1
    #     return root

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return 'None'
        return str(root.val) + ',' + str(self.serialize(root.left)) + ',' + str(self.serialize(root.right))

    @staticmethod
    def deserialize(data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def dfs(dataList):
            val = dataList.pop(0)
            if val == 'None':
                return None
            root = TreeNode(int(val))
            root.left = dfs(dataList)
            root.right = dfs(dataList)
            return root

        dataList = data.split(',')
        return dfs(dataList)

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

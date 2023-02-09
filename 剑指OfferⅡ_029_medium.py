# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/2/9 19:50
"""
"""
给定循环单调非递减列表中的一个点，写一个函数向这个列表中插入一个新元素 insertVal ，使这个列表仍然是循环升序的。
给定的可以是这个列表中任意一个顶点的指针，并不一定是这个列表中最小元素的指针。
如果有多个满足条件的插入位置，可以选择任意一个位置插入新的值，插入后整个列表仍然保持有序。
如果列表为空（给定的节点是 null），需要创建一个循环有序列表并返回这个节点。否则。请返回原先给定的节点。

示例 1：
输入：head = [3,4,1], insertVal = 2
输出：[3,4,1,2]
解释：在上图中，有一个包含三个元素的循环有序列表，你获得值为 3 的节点的指针，我们需要向表中插入元素 2 。新插入的节点应该在 1 和 
3 之间，插入之后，整个列表如上图所示，最后返回节点 3 。

示例 2：
输入：head = [], insertVal = 1
输出：[1]
解释：列表为空（给定的节点是 null），创建一个循环有序列表并返回这个节点。

示例 3：
输入：head = [1], insertVal = 0
输出：[1,0]
"""
"""
思路：如果循环链表为空，则插入一个新节点并将新节点的 next 指针指向自身，插入新节点之后得到只有一个节点的循环链表，该循环链表
一定是有序的，将插入的新节点作为新的头节点返回。
如果循环链表的头节点的 next 指针指向自身，则循环链表中只有一个节点，在头节点之后插入新节点，将头节点的 next 指针指向新节点，
将新节点的 next 指针指向头节点，此时循环链表中有两个节点且一定是有序的，返回头节点。
如果循环链表中的节点数大于 1，则需要从头节点开始遍历循环链表，寻找插入新节点的位置，使得插入新节点之后的循环链表仍然保持有序。
遍历过程中，如果找到插入新节点的位置，则有以下三种情况：
    curr.val≤insertVal≤next.val，此时新节点的值介于循环链表中的两个节点值之间，在 curr 和 next 之间插入新节点；
    curr.val>next.val 且 insertVal>curr.val，此时 curr 和 next 分别是循环链表中的值最大的节点和值最小的节点，insertVal 大于 
    curr 的节点值，因此新节点应该在 curr 的后面插入，即在 curr 和 next 之间插入新节点；
    curr.val>next.val 且 insertVal<next.val，此时 curr 和 next 分别是循环链表中的值最大的节点和值最小的节点，insertVal 小于 
    next 的节点值，因此新节点应该在 next 的前面插入，即在 curr 和 next 之间插入新节点。
"""


# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def insert(head: 'Node', insertVal: int) -> 'Node':
        node = Node(insertVal)
        if head is None:
            node.next = node
            return node
        if head.next == head:
            head.next = node
            node.next = head
            return head
        curr = head
        next = head.next
        while next != head:
            if curr.val <= insertVal <= next.val:
                break
            if curr.val > next.val:
                if insertVal > curr.val or insertVal < next.val:
                    break
            curr = curr.next
            next = next.next
        curr.next = node
        node.next = next
        return head

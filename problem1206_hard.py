# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/2/7 23:21
"""
import random

"""
不使用任何库函数，设计一个 跳表 。
跳表 是在 O(log(n)) 时间内完成增加、删除、搜索操作的数据结构。跳表相比于树堆与红黑树，其功能与性能相当，并且跳表的代码长度相较
下更短，其设计思想与链表相似。
例如，一个跳表包含 [30, 40, 50, 60, 70, 90] ，然后增加 80、45 到跳表中，以下图的方式操作：
Artyom Kalinin [CC BY-SA 3.0], via Wikimedia Commons
跳表中有很多层，每一层是一个短的链表。在第一层的作用下，增加、删除和搜索操作的时间复杂度不超过 O(n)。跳表的每一个操作的平均时间
复杂度是 O(log(n))，空间复杂度是 O(n)。
了解更多 : https://en.wikipedia.org/wiki/Skip_list
在本题中，你的设计应该要包含这些函数：
    bool search(int target) : 返回target是否存在于跳表中。
    void add(int num): 插入一个元素到跳表。
    bool erase(int num): 在跳表中删除一个值，如果 num 不存在，直接返回false. 如果存在多个 num ，删除其中任意一个即可。
注意，跳表中可能存在多个相同的值，你的代码需要处理这种情况。

示例 1:
输入
["Skiplist", "add", "add", "add", "search", "add", "search", "erase", "erase", "search"]
[[], [1], [2], [3], [0], [4], [1], [0], [1], [1]]
输出
[null, null, null, null, false, null, true, false, true, false]
解释
Skiplist skiplist = new Skiplist();
skiplist.add(1);
skiplist.add(2);
skiplist.add(3);
skiplist.search(0);   // 返回 false
skiplist.add(4);
skiplist.search(1);   // 返回 true
skiplist.erase(0);    // 返回 false，0 不在跳表中
skiplist.erase(1);    // 返回 true
skiplist.search(1);   // 返回 false，1 已被擦除
"""
"""
思路：
跳表在进行查找时，首先从当前的最高层 L(n) 层开始查找，在当前层水平地逐个比较直至当前节点的下一个节点大于等于目标节点，
然后移动至下一层进行查找，重复这个过程直至到达第一层。此时，若下一个节点是目标节点，则成功查找；反之，则元素不存在。
由于从高层往低层开始查找，由于低层出现的元素可能不会出现在高层，因此跳表在进行查找的过程中会跳过一些元素，相比于有序链表的查询，
跳表的查询速度会更快。
search：从跳表的当前的最大层数 level 层开始查找，在当前层水平地逐个比较直至当前节点的下一个节点大于等于目标节点，然后移动至
下一层进行查找，重复这个过程直至到达第 1 层。此时，若第 1 层的下一个节点的值等于 target，则返回 true；反之，则返回 false。
add：从跳表的当前的最大层数 level 层开始查找，在当前层水平地逐个比较直至当前节点的下一个节点大于等于目标节点，然后移动至下一层
进行查找，重复这个过程直至到达第 1 层。设新加入的节点为 newNode，我们需要计算出此次节点插入的层数 lv，如果 level 小于 lv，
则同时需要更新 level。我们用数组 update 保存每一层查找的最后一个节点，第 i 层最后的节点为 update[i]。我们将 newNode 的后续节点
指向 update[i] 的下一个节点，同时更新 update[i] 的后续节点为 newNode。
erase：首先我们需要查找当前元素是否存在跳表中。从跳表的当前的最大层数 level 层开始查找，在当前层水平地逐个比较直至当前节点的
下一个节点大于等于目标节点，然后移动至下一层进行查找，重复这个过程直至到达第 1 层。如果第 1 层的下一个节点不等于 num 时，则表示
当前元素不存在直接返回。我们用数组 update 保存每一层查找的最后一个节点，第 i 层最后的节点为 update[i]。此时第 i 层的下一个节点
的值为 num，则我们需要将其从跳表中将其删除。由于第 i 层的以 p 的概率出现在第 i+1 层，因此我们应当从第 1 层开始往上进行更新，将 
num 从 update[i] 的下一跳中删除，同时更新 update[i] 的后续节点，直到当前层的链表中没有出现 num 的节点为止。最后我们还需要更新
跳表中当前的最大层数 level。
"""

MAX_LEVEL = 32
P_FACTOR = 0.25


def random_level() -> int:
    lv = 1
    while lv < MAX_LEVEL and random.random() < P_FACTOR:
        lv += 1
    return lv


class SkiplistNode:
    __slots__ = 'val', 'forward'

    def __init__(self, val: int, max_level=MAX_LEVEL):
        self.val = val
        self.forward = [None] * max_level


class Skiplist:
    def __init__(self):
        self.head = SkiplistNode(-1)
        self.level = 0

    def search(self, target: int) -> bool:
        curr = self.head
        for i in range(self.level - 1, -1, -1):
            # 找到第 i 层小于且最接近 target 的元素
            while curr.forward[i] and curr.forward[i].val < target:
                curr = curr.forward[i]
        curr = curr.forward[0]
        # 检测当前元素的值是否等于 target
        return curr is not None and curr.val == target

    def add(self, num: int) -> None:
        update = [self.head] * MAX_LEVEL
        curr = self.head
        for i in range(self.level - 1, -1, -1):
            # 找到第 i 层小于且最接近 num 的元素
            while curr.forward[i] and curr.forward[i].val < num:
                curr = curr.forward[i]
            update[i] = curr
        lv = random_level()
        self.level = max(self.level, lv)
        new_node = SkiplistNode(num, lv)
        for i in range(lv):
            # 对第 i 层的状态进行更新，将当前元素的 forward 指向新的节点
            new_node.forward[i] = update[i].forward[i]
            update[i].forward[i] = new_node

    def erase(self, num: int) -> bool:
        update = [None] * MAX_LEVEL
        curr = self.head
        for i in range(self.level - 1, -1, -1):
            # 找到第 i 层小于且最接近 num 的元素
            while curr.forward[i] and curr.forward[i].val < num:
                curr = curr.forward[i]
            update[i] = curr
        curr = curr.forward[0]
        if curr is None or curr.val != num:  # 值不存在
            return False
        for i in range(self.level):
            if update[i].forward[i] != curr:
                break
            # 对第 i 层的状态进行更新，将 forward 指向被删除节点的下一跳
            update[i].forward[i] = curr.forward[i]
        # 更新当前的 level
        while self.level > 1 and self.head.forward[self.level - 1] is None:
            self.level -= 1
        return True

# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)

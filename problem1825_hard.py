# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/1/18 18:48
"""
from collections import deque

from sortedcontainers import SortedList

"""
给你两个整数 m 和 k ，以及数据流形式的若干整数。你需要实现一个数据结构，计算这个数据流的 MK 平均值 。
MK 平均值 按照如下步骤计算：
    如果数据流中的整数少于 m 个，MK 平均值 为 -1 ，否则将数据流中最后 m 个元素拷贝到一个独立的容器中。
    从这个容器中删除最小的 k 个数和最大的 k 个数。
    计算剩余元素的平均值，并 向下取整到最近的整数 。
请你实现 MKAverage 类：
    MKAverage(int m, int k) 用一个空的数据流和两个整数 m 和 k 初始化 MKAverage 对象。
    void addElement(int num) 往数据流中插入一个新的元素 num 。
    int calculateMKAverage() 对当前的数据流计算并返回 MK 平均数 ，结果需 向下取整到最近的整数 。

示例 1：
输入：
["MKAverage", "addElement", "addElement", "calculateMKAverage", "addElement", "calculateMKAverage", "addElement", 
"addElement", "addElement", "calculateMKAverage"]
[[3, 1], [3], [1], [], [10], [], [5], [5], [5], []]
输出：
[null, null, null, -1, null, 3, null, null, null, 5]
解释：
MKAverage obj = new MKAverage(3, 1); 
obj.addElement(3);        // 当前元素为 [3]
obj.addElement(1);        // 当前元素为 [3,1]
obj.calculateMKAverage(); // 返回 -1 ，因为 m = 3 ，但数据流中只有 2 个元素
obj.addElement(10);       // 当前元素为 [3,1,10]
obj.calculateMKAverage(); // 最后 3 个元素为 [3,1,10]
                          // 删除最小以及最大的 1 个元素后，容器为 [3]
                          // [3] 的平均值等于 3/1 = 3 ，故返回 3
obj.addElement(5);        // 当前元素为 [3,1,10,5]
obj.addElement(5);        // 当前元素为 [3,1,10,5,5]
obj.addElement(5);        // 当前元素为 [3,1,10,5,5,5]
obj.calculateMKAverage(); // 最后 3 个元素为 [5,5,5]
                          // 删除最小以及最大的 1 个元素后，容器为 [5]
                          // [5] 的平均值等于 5/1 = 5 ，故返回 5
"""
"""
思路：
如果 low 为空，或者 num≤max(lo2)，则将 num 加入 low 中；否则如果 high 为空，或者 num≥min(high)，则将 num 加入 high 中；否则
将 num 加入 mid 中，同时将 num 的值加到 s 中。
接下来将 num 加入队列 q 中，如果此时队列 q 的长度大于 m，则将队首元素 x 从队列 q 中移除，接下来从 low, mid 或 high 中选择其中
一个包含 x 的集合，将 x 从该集合中移除，如果该集合为 mid，则将 s 减去 x 的值。
如果 low 的长度大于 k，则循环将 low 中的最大值 max(low) 从 low 中移除，将 max(low) 加入 mid 中，同时将 s 加上 max(low) 的值。
如果 high 的长度大于 k，则循环将 high 中的最小值 min(high) 从 high 中移除，将 min(high) 加入 mid 中，同时将 s 加上 min(high) 
的值。
如果low 的长度小于 k，并且 mid 不为空，则循环将 mid 中的最小值 min(mid) 从 mid 中移除，将 min(mid) 加入 low 中，同时将 
s 减去 min(mid) 的值。
如果 high 的长度小于 k，并且 mid 不为空，则循环将 mid 中的最大值 max(mid) 从 mid 中移除，将 max(mid) 
加入 high 中，同时将 s 减去 max(mid) 的值。
"""


class MKAverage:

    def __init__(self, m: int, k: int):
        self.m = m
        self.k = k
        self.s = 0
        self.q = deque()
        self.low = SortedList()
        self.mid = SortedList()
        self.high = SortedList()

    def addElement(self, num: int) -> None:
        if not self.low or num <= self.low[-1]:
            self.low.add(num)
        elif not self.high or num >= self.high[0]:
            self.high.add(num)
        else:
            self.mid.add(num)
            self.s += num
        self.q.append(num)
        if len(self.q) > self.m:
            x = self.q.popleft()
            if x in self.low:
                self.low.remove(x)
            elif x in self.high:
                self.high.remove(x)
            else:
                self.mid.remove(x)
                self.s -= x
        while len(self.low) > self.k:
            x = self.low.pop()
            self.mid.add(x)
            self.s += x
        while len(self.high) > self.k:
            x = self.high.pop(0)
            self.mid.add(x)
            self.s += x
        while len(self.low) < self.k and self.mid:
            x = self.mid.pop(0)
            self.low.add(x)
            self.s -= x
        while len(self.high) < self.k and self.mid:
            x = self.mid.pop()
            self.high.add(x)
            self.s -= x

    def calculateMKAverage(self) -> int:
        return -1 if len(self.q) < self.m else self.s // (self.m - 2 * self.k)

# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()

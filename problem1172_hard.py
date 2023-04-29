# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/4/29 23:07
"""
from sortedcontainers import SortedSet

"""
我们把无限数量 ∞ 的栈排成一行，按从左到右的次序从 0 开始编号。每个栈的的最大容量 capacity 都相同。
实现一个叫「餐盘」的类 DinnerPlates：
    DinnerPlates(int capacity) - 给出栈的最大容量 capacity。
    void push(int val) - 将给出的正整数 val 推入 从左往右第一个 没有满的栈。
    int pop() - 返回 从右往左第一个 非空栈顶部的值，并将其从栈中删除；如果所有的栈都是空的，请返回 -1。
    int popAtStack(int index) - 返回编号 index 的栈顶部的值，并将其从栈中删除；如果编号 index 的栈是空的，请返回 -1。

示例：
输入： 
["DinnerPlates","push","push","push","push","push","popAtStack","push","push","popAtStack","popAtStack","pop","pop","pop","pop","pop"]
[[2],[1],[2],[3],[4],[5],[0],[20],[21],[0],[2],[],[],[],[],[]]
输出：
[null,null,null,null,null,null,2,null,null,20,21,5,4,3,1,-1]

解释：
DinnerPlates D = DinnerPlates(2);  // 初始化，栈最大容量 capacity = 2
D.push(1);
D.push(2);
D.push(3);
D.push(4);
D.push(5);         // 栈的现状为：    2  4
                                    1  3  5
                                    ﹈ ﹈ ﹈
D.popAtStack(0);   // 返回 2。栈的现状为：      4
                                          1  3  5
                                          ﹈ ﹈ ﹈
D.push(20);        // 栈的现状为：  20  4
                                   1  3  5
                                   ﹈ ﹈ ﹈
D.push(21);        // 栈的现状为：  20  4 21
                                   1  3  5
                                   ﹈ ﹈ ﹈
D.popAtStack(0);   // 返回 20。栈的现状为：       4 21
                                            1  3  5
                                            ﹈ ﹈ ﹈
D.popAtStack(2);   // 返回 21。栈的现状为：       4
                                            1  3  5
                                            ﹈ ﹈ ﹈ 
D.pop()            // 返回 5。栈的现状为：        4
                                            1  3 
                                            ﹈ ﹈  
D.pop()            // 返回 4。栈的现状为：    1  3 
                                           ﹈ ﹈   
D.pop()            // 返回 3。栈的现状为：    1 
                                           ﹈   
D.pop()            // 返回 1。现在没有栈。
D.pop()            // 返回 -1。仍然没有栈。
"""
"""
思路：
我们定义以下数据结构或变量：
    capacity：每个栈的容量；
    stacks：栈数组，用于存储所有的栈，其中每个栈的最大容量都是 capacity；
    not_full：有序集合，用于存储所有未满的栈在栈数组中的下标。
对于 push(val) 操作：
    我们首先判断 not_full 是否为空，如果为空，则说明没有未满的栈，需要新建一个栈，然后将 val 压入该栈中，此时判断容量 capacity 
    是否大于 1，如果大于 1，则将该栈的下标加入 not_full 中。
    如果 not_full 不为空，则说明有未满的栈，我们取出 not_full 中最小的下标 index，将 val 压入 stacks[index] 中，此时如果 
    stacks[index] 的容量等于 capacity，则将 index 从 not_full 中删除。
对于 popAtStack(index) 操作：
    我们首先判断 index 是否在 stacks 的下标范围内，如果不在，则直接返回 −1。如果 stacks[index] 为空，同样直接返回 −1。
    如果 stacks[index] 不为空，则弹出 stacks[index] 的栈顶元素 val。如果 index 等于 stacks 的长度减 1，则说明 stacks[index] 
    是最后一个栈，如果为空，我们循环将最后一个栈的下标从 not_full 中移出，并且在栈数组 stacks 中移除最后一个栈，直到最后一个栈
    不为空、或者栈数组 stacks 为空为止。否则，如果 stacks[index] 不是最后一个栈，我们将 index 加入 not_full 中。
    最后返回 val。
对于 pop() 操作：
    我们直接调用 popAtStack(stacks.length - 1) 即可。
"""


class DinnerPlates:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stacks = []
        self.not_full = SortedSet()

    def push(self, val: int) -> None:
        if not self.not_full:
            self.stacks.append([val])
            if self.capacity > 1:
                self.not_full.add(len(self.stacks) - 1)
        else:
            index = self.not_full[0]
            self.stacks[index].append(val)
            if len(self.stacks[index]) == self.capacity:
                self.not_full.discard(index)

    def pop(self) -> int:
        return self.popAtStack(len(self.stacks) - 1)

    def popAtStack(self, index: int) -> int:
        if index < 0 or index >= len(self.stacks) or not self.stacks[index]:
            return -1
        val = self.stacks[index].pop()
        if index == len(self.stacks) - 1 and not self.stacks[-1]:
            while self.stacks and not self.stacks[-1]:
                self.not_full.discard(len(self.stacks) - 1)
                self.stacks.pop()
        else:
            self.not_full.add(index)
        return val

# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)

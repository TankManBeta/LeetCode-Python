# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/11/30 10:58
"""
"""
设计一个类似堆栈的数据结构，将元素推入堆栈，并从堆栈中弹出出现频率最高的元素。
实现 FreqStack 类:
FreqStack() 构造一个空的堆栈。
void push(int val) 将一个整数 val 压入栈顶。
int pop() 删除并返回堆栈中出现频率最高的元素。
如果出现频率最高的元素不只一个，则移除并返回最接近栈顶的元素。

示例 1：
输入：
["FreqStack","push","push","push","push","push","push","pop","pop","pop","pop"],
[[],[5],[7],[5],[7],[4],[5],[],[],[],[]]
输出：[null,null,null,null,null,null,null,5,7,5,4]
解释：
FreqStack = new FreqStack();
freqStack.push (5);//堆栈为 [5]
freqStack.push (7);//堆栈是 [5,7]
freqStack.push (5);//堆栈是 [5,7,5]
freqStack.push (7);//堆栈是 [5,7,5,7]
freqStack.push (4);//堆栈是 [5,7,5,7,4]
freqStack.push (5);//堆栈是 [5,7,5,7,4,5]
freqStack.pop ();//返回 5 ，因为 5 出现频率最高。堆栈变成 [5,7,5,7,4]。
freqStack.pop ();//返回 7 ，因为 5 和 7 出现频率最高，但7最接近顶部。堆栈变成 [5,7,5,4]。
freqStack.pop ();//返回 5 ，因为 5 出现频率最高。堆栈变成 [5,7,4]。
freqStack.pop ();//返回 4 ，因为 4, 5 和 7 出现频率最高，但 4 是最接近顶部的。堆栈变成 [5,7]。
"""
"""
思路：哈希表+栈，把频率（出现次数）不同的元素，压入不同的栈中。每次出栈时，弹出含有频率最高元素的栈的栈顶。（一个数字出现过n次，
那么它在频率为1的栈、频率为2的栈、频率为n的栈都要出现）同时，为了知道每个元素的频率，还需要用一个哈希表来实时维护。
"""


class FreqStack:

    def __init__(self):
        self.count_dict = {}
        self.stacks = []

    def push(self, val: int) -> None:
        already = self.count_dict.get(val, 0)
        if already == len(self.stacks):
            self.stacks.append([val])
        else:
            self.stacks[already].append(val)
        self.count_dict[val] = already + 1

    def pop(self) -> int:
        num = self.stacks[-1].pop()
        if len(self.stacks[-1]) == 0:
            self.stacks.pop()
        self.count_dict[num] -= 1
        return num

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()

# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/5/16 11:47
"""

"""
定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。

示例:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.min();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.min();   --> 返回 -2.
"""
"""
思路：
（1）使用额外的辅助栈，每次新push元素进来之后，就把当前元素和栈顶元素之间的最小值放入辅助栈中。这样pop的时候辅助栈同时一起pop。
（2）不使用额外的辅助栈。栈中存放的都是push进来的元素x与当前最小值min的差值，如果算出来的x-min<0，则说明当前元素比当前最小值
还要值，更新当前最小值。pop的时候需要注意，要是当前栈顶元素<0，说明当前最小值会受到影响，需要重新将其还原。
"""


# class MinStack:
#     def __init__(self):
#         self.stack = []
#         self.min_stack = [math.inf]

#     def push(self, x: int) -> None:
#         self.stack.append(x)
#         self.min_stack.append(min(x, self.min_stack[-1]))

#     def pop(self) -> None:
#         self.stack.pop()
#         self.min_stack.pop()

#     def top(self) -> int:
#         return self.stack[-1]

#     def min(self) -> int:
#         return self.min_stack[-1]

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_val = 0

    def push(self, x: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min_val = x
        else:
            self.stack.append(x-self.min_val)
            self.min_val = min(self.min_val, x)

    def pop(self) -> None:
        if self.stack[-1] < 0:
            self.min_val = self.min_val-self.stack[-1]
        self.stack.pop()

    def top(self) -> int:
        if self.stack[-1] < 0:
            return self.min_val
        else:
            return self.stack[-1] + self.min_val

    def min(self) -> int:
        return self.min_val

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()

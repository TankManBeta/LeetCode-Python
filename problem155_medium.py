# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/3/18 10:15
"""
"""
设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。
实现 MinStack 类:
    MinStack() 初始化堆栈对象。
    void push(int val) 将元素val推入堆栈。
    void pop() 删除堆栈顶部的元素。
    int top() 获取堆栈顶部的元素。
    int getMin() 获取堆栈中的最小元素。

输入：
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]
输出：
[null,null,null,null,-3,null,0,-2]
解释：
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.
"""
"""
思路：
（1）使用辅助栈min_stack保存当前最小元素，然后和栈一起pop，push
（2）不使用额外空间，栈里存当前值与最小值的差值即可。push时，如果差值小于0说明当前数才是最小值，更新最小值；pop时，如果当前栈顶
小于0，说明当前栈顶的是最小值，pop完之后新的最小值需要更新，新的最小值更新为min_val-diff；为什么可以这样更新，因为diff是当前值
减去最小值得到的，如果栈顶小于0，说明当前值减去上一步的最小值得到了这个差，所以可以返回回去
"""


class MinStack(object):

    # def __init__(self):
    #     self.stack = []
    #     self.min_stack = [sys.maxsize]

    # def push(self, val):
    #     """
    #     :type val: int
    #     :rtype: None
    #     """
    #     self.stack.append(val)
    #     self.min_stack.append(min(self.min_stack[-1], val))

    # def pop(self):
    #     """
    #     :rtype: None
    #     """
    #     self.stack.pop()
    #     self.min_stack.pop()

    # def top(self):
    #     """
    #     :rtype: int
    #     """
    #     return self.stack[-1]

    # def getMin(self):
    #     """
    #     :rtype: int
    #     """
    #     return self.min_stack[-1]

    def __init__(self):
        self.stack = []
        self.min_val = -1

    def push(self, val):
        if not self.stack:
            self.stack.append(0)
            self.min_val = val
        else:
            diff = val - self.min_val
            self.stack.append(diff)
            if diff < 0:
                self.min_val = val

    def pop(self):
        diff = self.stack.pop()
        if diff < 0:
            pop_val = self.min_val
            self.min_val = self.min_val - diff
        else:
            pop_val = self.min_val + diff
        return pop_val

    def top(self):
        return self.min_val if self.stack[-1] < 0 else self.min_val + self.stack[-1]

    def getMin(self):
        return self.min_val

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

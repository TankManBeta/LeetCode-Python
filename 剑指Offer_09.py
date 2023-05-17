# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/5/16 11:32
"""
"""
用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，分别完成在队列尾部插入整数和在队列头部删除
整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 ) 

示例 1：
输入：
["CQueue","appendTail","deleteHead","deleteHead","deleteHead"]
[[],[3],[],[],[]]
输出：[null,null,3,-1,-1]

示例 2：
输入：
["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
[[],[],[5],[2],[],[]]
输出：[null,-1,null,null,5,2]
"""
"""
思路：队列是先进先出的数据结构，而栈是先进后出的数据结构。所以思路很简单，就通过一个辅助栈将主栈的元素反序，具体的做法是：对于
删除对头来说，由于我们将栈的结构反序了，所以只需要删除栈顶即可。对于插入元素来说，我们将主栈中的元素全部放入辅助栈，然后将新的
值放入主栈，最后再将辅助栈的元素全部放入主栈即可。
举例如下：
插入1：主栈[1]，辅助栈[]
插入2：主栈[]，辅助栈[1]；主栈[2]，辅助栈[1]；主栈[2,1]，辅助栈[]
插入3：主栈[]，辅助栈[1,2]；主栈[3]，辅助栈[1,2]；主栈[3,2,1]，辅助栈[]
"""


class CQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def appendTail(self, value: int) -> None:
        # 1 -> 2
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        # add value
        self.stack1.append(value)
        # 1 <- 2
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return self.stack1

    def deleteHead(self) -> int:
        if not self.stack1:
            return -1
        return self.stack1.pop()

# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()

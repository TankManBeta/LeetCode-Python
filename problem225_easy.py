# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/4/8 10:07
"""
import collections

"""
请你仅使用两个队列实现一个后入先出（LIFO）的栈，并支持普通栈的全部四种操作（push、top、pop 和 empty）。
实现 MyStack 类：
    void push(int x) 将元素 x 压入栈顶。
    int pop() 移除并返回栈顶元素。
    int top() 返回栈顶元素。
    boolean empty() 如果栈是空的，返回 true ；否则，返回 false 。
注意：
你只能使用队列的基本操作 —— 也就是 push to back、peek/pop from front、size 和 is empty 这些操作。
你所使用的语言也许不支持队列。 你可以使用 list （列表）或者 deque（双端队列）来模拟一个队列 , 只要是标准的队列操作即可。

输入：
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]
输出：
[null, null, null, 2, 2, false]

解释：
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // 返回 2
myStack.pop(); // 返回 2
myStack.empty(); // 返回 False
"""
"""
思路：
（1）两个队列模拟，先把要push的元素放在queue2中，然后把queue1中的元素全部放到queue2中即可，然后交换queue1和queue2
（2）一个队列模拟，先记住要push之前queue的长度n，然后push新的元素，然后再把前n个全部重新入队
"""


class MyStack(object):

    def __init__(self):
        # self.queue1 = collections.deque()
        # self.queue2 = collections.deque()

        self.queue = collections.deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        # self.queue2.append(x)
        # while self.queue1:
        #     self.queue2.append(self.queue1.popleft())
        # self.queue1, self.queue2 = self.queue2, self.queue1

        n = len(self.queue)
        self.queue.append(x)
        for _ in range(n):
            temp = self.queue.popleft()
            self.queue.append(temp)

    def pop(self):
        """
        :rtype: int
        """
        # return self.queue1.popleft()

        return self.queue.popleft()

    def top(self):
        """
        :rtype: int
        """
        # return self.queue1[0]

        return self.queue[0]

    def empty(self):
        """
        :rtype: bool
        """
        # return not self.queue1

        return not self.queue


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/6/11 15:26
"""
"""
请定义一个队列并实现函数 max_value 得到队列里的最大值，要求函数max_value、push_back 和 pop_front 的均摊时间复杂度都是O(1)。
若队列为空，pop_front 和 max_value 需要返回 -1

示例 1：
输入: 
["MaxQueue","push_back","push_back","max_value","pop_front","max_value"]
[[],[1],[2],[],[],[]]
输出: [null,null,null,2,1,2]

示例 2：
输入: 
["MaxQueue","pop_front","max_value"]
[[],[],[]]
输出: [null,-1,-1]
"""
"""
思路：常规思路出现的问题是：当出队时，这个方法会造成信息丢失，即当最大值出队后，我们无法知道队列里的下一个最大值。因此我们只需
记住当前最大值出队后，队列里的下一个最大值即可。具体方法是使用一个双端队列 deque，在每次入队时，如果 deque 队尾元素小于即将入队
的元素 value，则将小于 value 的元素全部出队后，再将 value 入队；否则直接入队。
"""

import queue


class MaxQueue:

    def __init__(self):
        self.queue = queue.Queue()
        self.deque = queue.deque()

    def max_value(self) -> int:
        if self.deque:
            return self.deque[0]
        else:
            return -1
        # return self.deque[0] if self.deque else -1 或者这样写

    def push_back(self, value: int) -> None:
        while self.deque and self.deque[-1] < value:
            self.deque.pop()
        self.deque.append(value)
        self.queue.put(value)

    def pop_front(self) -> int:
        if not self.deque:
            return -1
        ans = self.queue.get()
        if ans == self.deque[0]:
            self.deque.popleft()
        return ans

# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()

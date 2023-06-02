# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/6/1 10:32
"""
import heapq

"""
如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出
偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。
例如，
[2,3,4] 的中位数是 3
[2,3] 的中位数是 (2 + 3) / 2 = 2.5
设计一个支持以下两种操作的数据结构：
    void addNum(int num) - 从数据流中添加一个整数到数据结构中。
    double findMedian() - 返回目前所有元素的中位数。

示例 1：
输入：
["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]
[[],[1],[2],[],[3],[]]
输出：[null,null,null,1.50000,null,2.00000]

示例 2：
输入：
["MedianFinder","addNum","findMedian","addNum","findMedian"]
[[],[2],[],[3],[]]
输出：[null,null,2.00000,null,2.50000]
"""
"""
思路：建立两个堆，一个大根堆，一个小根堆，每次add的时候先看两个堆的长度是否一样长，如果一样长则先将num与大根堆的堆顶比较，如果
比大根堆的堆顶小，直接放入大根堆；如果比大根堆的堆顶大，先放入小根堆，然后把小根堆的堆顶放入大根堆；如果两个堆的长度不一样长，
则先放入大根堆，然后把大根堆的堆顶弹出并放入小根堆。读取的时候如果大根堆小根堆长度不一样，返回大根堆的堆顶，否则返回大小根堆堆顶
的平均值。
"""


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.heap1 = []
        self.heap2 = []

    def addNum(self, num: int) -> None:
        if not self.heap1:
            heapq.heappush(self.heap1, -num)
        else:
            if len(self.heap1) == len(self.heap2):
                if num <= -self.heap1[0]:
                    heapq.heappush(self.heap1, -num)
                else:
                    heapq.heappush(self.heap1, -heapq.heappushpop(self.heap2, num))
            else:
                heapq.heappush(self.heap2, -heapq.heappushpop(self.heap1, -num))

    def findMedian(self) -> float:
        return -self.heap1[0] if len(self.heap1) != len(self.heap2) else (-self.heap1[0] + self.heap2[0]) / 2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

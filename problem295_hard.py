# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/12/4 17:54
"""
import heapq

from sortedcontainers import SortedList

"""
中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。
例如，
[2,3,4] 的中位数是 3
[2,3] 的中位数是 (2 + 3) / 2 = 2.5
设计一个支持以下两种操作的数据结构：
void addNum(int num) - 从数据流中添加一个整数到数据结构中。
double findMedian() - 返回目前所有元素的中位数。

示例：
addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2
"""
"""
思路：
（1）优先队列，queMin存储小于等于中位数的所有数，queMax存储大于中位数的所有数。如果两个队列的长度相同时，如果都为空，直接将num
放入queMin中；如果num小于等于queMin的堆顶，则也将其放入queMin中；如果num大于queMin的堆顶，说明他应该放在queMax中，此时需要将
queMax的堆顶放入queMin中。如果两个队列长度不相同，如果num大于等于queMin的堆顶，则直接放入queMax中；否则将queMin的堆顶放入queMax
中，同时将num放入queMin中。
（2）有序集合，升序排序，根据奇偶来取中位数
"""


class MedianFinder:

    # def __init__(self):
    #     self.queMin = list()
    #     self.queMax = list()
    #
    # def addNum(self, num: int) -> None:
    #     queMin_ = self.queMin
    #     queMax_ = self.queMax
    #
    #     if len(queMin_) == len(queMax_):
    #         if not queMin_ or num <= -queMin_[0]:
    #             heapq.heappush(queMin_, -num)
    #         else:
    #             heapq.heappush(queMax_, num)
    #             heapq.heappush(queMin_, -heapq.heappop(queMax_))
    #     else:
    #         if num >= -queMin_[0]:
    #             heapq.heappush(queMax_, num)
    #         else:
    #             heapq.heappush(queMax_, -heapq.heappop(queMin_))
    #             heapq.heappush(queMin_, -num)
    #
    # def findMedian(self) -> float:
    #     queMin_ = self.queMin
    #     queMax_ = self.queMax
    #
    #     if len(queMin_) > len(queMax_):
    #         return -queMin_[0]
    #     return (-queMin_[0] + queMax_[0]) / 2

    def __init__(self):
        self.lst = SortedList()

    def addNum(self, num: int) -> None:
        self.lst.add(num)

    def findMedian(self) -> float:
        n = len(self.lst)
        k = n // 2
        if n % 2:
            return self.lst[k]
        return (self.lst[k - 1] + self.lst[k]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

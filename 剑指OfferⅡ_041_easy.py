# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/2/9 20:37
"""
from collections import deque

"""
给定一个整数数据流和一个窗口大小，根据该滑动窗口的大小，计算滑动窗口里所有数字的平均值。
实现 MovingAverage 类：
    MovingAverage(int size) 用窗口大小 size 初始化对象。
    double next(int val) 成员函数 next 每次调用的时候都会往滑动窗口增加一个整数，请计算并返回数据流中最后 size 个值的移动平均值，
    即滑动窗口里所有数字的平均值。

示例：
输入：
inputs = ["MovingAverage", "next", "next", "next", "next"]
inputs = [[3], [1], [10], [3], [5]]
输出：
[null, 1.0, 5.5, 4.66667, 6.0]
解释：
MovingAverage movingAverage = new MovingAverage(3);
movingAverage.next(1); // 返回 1.0 = 1 / 1
movingAverage.next(10); // 返回 5.5 = (1 + 10) / 2
movingAverage.next(3); // 返回 4.66667 = (1 + 10 + 3) / 3
movingAverage.next(5); // 返回 6.0 = (10 + 3 + 5) / 3
"""
"""
思路：初始时，队列为空，滑动窗口的大小设为给定的参数 size，滑动窗口的数字之和为 0。每次调用 next 时，需要将 val 添加到滑动窗口中，
同时确保滑动窗口中的数字个数不超过 size，如果数字个数超过 size 则需要将多余的数字移除，在添加和移除数字的同时需要更新滑动窗口的数字
之和。由于每次调用只会将一个数字添加到滑动窗口中，因此每次调用最多只需要将一个多余的数字移除。
"""


class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.sum = 0
        self.q = deque()

    def next(self, val: int) -> float:
        if len(self.q) == self.size:
            self.sum -= self.q.popleft()
        self.sum += val
        self.q.append(val)
        return self.sum / len(self.q)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

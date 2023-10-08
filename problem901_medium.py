# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/10/7 21:18
"""
"""
设计一个算法收集某些股票的每日报价，并返回该股票当日价格的 跨度 。
当日股票价格的 跨度 被定义为股票价格小于或等于今天价格的最大连续日数（从今天开始往回数，包括今天）。
例如，如果未来 7 天股票的价格是 [100,80,60,70,60,75,85]，那么股票跨度将是 [1,1,1,2,1,4,6] 。
实现 StockSpanner 类：
StockSpanner() 初始化类对象。
int next(int price) 给出今天的股价 price ，返回该股票当日价格的 跨度 。

示例：
输入：
["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
[[], [100], [80], [60], [70], [60], [75], [85]]
输出：
[null, 1, 1, 1, 2, 1, 4, 6]
解释：
StockSpanner stockSpanner = new StockSpanner();
stockSpanner.next(100); // 返回 1
stockSpanner.next(80);  // 返回 1
stockSpanner.next(60);  // 返回 1
stockSpanner.next(70);  // 返回 2
stockSpanner.next(60);  // 返回 1
stockSpanner.next(75);  // 返回 4 ，因为截至今天的最后 4 个股价 (包括今天的股价 75) 都小于或等于今天的股价。
stockSpanner.next(85);  // 返回 6
"""
"""
思路：根据题目描述，我们可以知道，对于当日价格 price，从这个价格开始往前找，找到第一个比这个价格大的价格，这两个价格的下标差 cnt 就是当日
价格的跨度。这实际上是经典的单调栈模型，找出左侧第一个比当前元素大的元素。我们维护一个从栈底到栈顶价格单调递减的栈，栈中每个元素存放的是 
(price,cnt) 数据对，其中 pricep 表示价格，而 cnt 表示当前价格的跨度。出现价格 price 时，我们将其与栈顶元素进行比较，如果栈顶元素的价格
小于等于 price，则将当日价格的跨度 cnt 加上栈顶元素的跨度，然后将栈顶元素出栈，直到栈顶元素的价格大于 price，或者栈为空为止。最后将 
(price,cnt) 入栈，返回 cnt 即可。
"""


class StockSpanner:
    def __init__(self):
        self.stk = []

    def next(self, price: int) -> int:
        cnt = 1
        while self.stk and self.stk[-1][0] <= price:
            cnt += self.stk.pop()[1]
        self.stk.append((price, cnt))
        return cnt

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/6/1 10:02
"""
from typing import List

"""
给你一个正整数数组 price ，其中 price[i] 表示第 i 类糖果的价格，另给你一个正整数 k 。
商店组合 k 类 不同 糖果打包成礼盒出售。礼盒的 甜蜜度 是礼盒中任意两种糖果 价格 绝对差的最小值。
返回礼盒的 最大 甜蜜度。

示例 1：
输入：price = [13,5,1,8,21,2], k = 3
输出：8
解释：选出价格分别为 [13,5,21] 的三类糖果。
礼盒的甜蜜度为 min(|13 - 5|, |13 - 21|, |5 - 21|) = min(8, 8, 16) = 8 。
可以证明能够取得的最大甜蜜度就是 8 。

示例 2：
输入：price = [1,3,1], k = 2
输出：2
解释：选出价格分别为 [1,3] 的两类糖果。 
礼盒的甜蜜度为 min(|1 - 3|) = min(2) = 2 。
可以证明能够取得的最大甜蜜度就是 2 。

示例 3：
输入：price = [7,7,7,7], k = 2
输出：0
解释：从现有的糖果中任选两类糖果，甜蜜度都会是 0 。
"""
"""
思路：排序+贪心。如果甜蜜度x可行的话，那么甜蜜度大于x的也可行。所以我们先排序，然后枚举甜蜜度，定义二分查找的左右边界 l=0, 
r=price[n−1]−price[0]。每一次，我们计算出当前的中间值 mid=⌊l+r+1⌋//2，以 mid 作为甜蜜度，判断是否可行。若可行，那么我们将左边界 
l 更新为 mid，否则将右边界 r 更新为 mid−1。最后返回 l 即可。那么问题的关键转化为：判断一个甜蜜度是否可行，我们通过函数 check(x) 
来实现。函数 check(x) 的执行逻辑如下：定义一个变量 cnt 表示当前已经选取的糖果的数量，初始值为 0，定义一个变量 pre 表示上一个
选取的糖果的价格，初始值为 −x。然后我们遍历排好序的数组 price，对于每一个糖果的价格 cur，如果 cur−pre≥x，那么我们就选取这个糖果，
将 pre 更新为 cur，并将 cnt 加一。最后判断 cnt 是否大于等于 k，如果是，那么返回 true，否则返回 false。
"""


class Solution:
    @staticmethod
    def maximumTastiness(price: List[int], k: int) -> int:
        price = sorted(price)
        i = 0
        j = price[-1] - price[0]

        def check(x):
            cnt = 0
            pre = -x
            for p in price:
                tmp = p - pre
                if tmp >= x:
                    cnt += 1
                    pre = p
            return cnt >= k

        while i < j:
            mid = (i + j + 1) // 2
            if check(mid):
                i = mid
            else:
                j = mid - 1

        return i

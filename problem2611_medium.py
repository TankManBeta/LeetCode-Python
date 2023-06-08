# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/6/7 16:52
"""
from typing import List

"""
有两只老鼠和 n 块不同类型的奶酪，每块奶酪都只能被其中一只老鼠吃掉。
下标为 i 处的奶酪被吃掉的得分为：
    如果第一只老鼠吃掉，则得分为 reward1[i] 。
    如果第二只老鼠吃掉，则得分为 reward2[i] 。
给你一个正整数数组 reward1 ，一个正整数数组 reward2 ，和一个非负整数 k 。
请你返回第一只老鼠恰好吃掉 k 块奶酪的情况下，最大 得分为多少。

示例 1：
输入：reward1 = [1,1,3,4], reward2 = [4,4,1,1], k = 2
输出：15
解释：这个例子中，第一只老鼠吃掉第 2 和 3 块奶酪（下标从 0 开始），第二只老鼠吃掉第 0 和 1 块奶酪。
总得分为 4 + 4 + 3 + 4 = 15 。
15 是最高得分。

示例 2：
输入：reward1 = [1,1], reward2 = [1,1], k = 2
输出：2
解释：这个例子中，第一只老鼠吃掉第 0 和 1 块奶酪（下标从 0 开始），第二只老鼠不吃任何奶酪。
总得分为 1 + 1 = 2 。
2 是最高得分。
"""
"""
思路：排序+贪心。我们现在假设所有的奶酪都被第二只老鼠吃了，则得分和为sum(reward2)，现在我们要选一块给第一只老鼠吃，则变化量为
reward1[i]-reward2[i]，所以我们构造一个diff数组，然后对这个数组进行排序，选前k个最大的给第一只老鼠吃即可。
"""


class Solution:
    @staticmethod
    def miceAndCheese(reward1: List[int], reward2: List[int], k: int) -> int:
        n = len(reward1)
        diff = [reward1[i] - reward2[i] for i in range(n)]
        ans = sum(reward2)
        diff = sorted(diff, reverse=True)
        for i in range(k):
            ans += diff[i]
        return ans

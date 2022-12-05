# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/12/4 12:20
"""
from typing import List

"""
你打算做甜点，现在需要购买配料。目前共有 n 种冰激凌基料和 m 种配料可供选购。而制作甜点需要遵循以下几条规则：
必须选择 一种 冰激凌基料。
可以添加 一种或多种 配料，也可以不添加任何配料。
每种类型的配料 最多两份 。
给你以下三个输入：
baseCosts ，一个长度为 n 的整数数组，其中每个 baseCosts[i] 表示第 i 种冰激凌基料的价格。
toppingCosts，一个长度为 m 的整数数组，其中每个 toppingCosts[i] 表示 一份 第 i 种冰激凌配料的价格。
target ，一个整数，表示你制作甜点的目标价格。
你希望自己做的甜点总成本尽可能接近目标价格 target 。
返回最接近 target 的甜点成本。如果有多种方案，返回 成本相对较低 的一种。

示例 1：
输入：baseCosts = [1,7], toppingCosts = [3,4], target = 10
输出：10
解释：考虑下面的方案组合（所有下标均从 0 开始）：
- 选择 1 号基料：成本 7
- 选择 1 份 0 号配料：成本 1 x 3 = 3
- 选择 0 份 1 号配料：成本 0 x 4 = 0
总成本：7 + 3 + 0 = 10 。

示例 2：
输入：baseCosts = [2,3], toppingCosts = [4,5,100], target = 18
输出：17
解释：考虑下面的方案组合（所有下标均从 0 开始）：
- 选择 1 号基料：成本 3
- 选择 1 份 0 号配料：成本 1 x 4 = 4
- 选择 2 份 1 号配料：成本 2 x 5 = 10
- 选择 0 份 2 号配料：成本 0 x 100 = 0
总成本：3 + 4 + 10 + 0 = 17 。不存在总成本为 18 的甜点制作方案。

示例 3：
输入：baseCosts = [3,10], toppingCosts = [2,5], target = 9
输出：8
解释：可以制作总成本为 8 和 10 的甜点。返回 8 ，因为这是成本更低的方案。

示例 4：
输入：baseCosts = [10], toppingCosts = [1], target = 1
输出：10
解释：注意，你可以选择不添加任何配料，但你必须选择一种基料。
"""
"""
思路：
（1）枚举所有的成本情况，然后二分查找即可。对于每一种配料，选择基料，然后将新生成的成本也加入到基料的集合当中，依次类推就能找到
所有成本的集合。
（2）dfs。生成配料所有可能的列表，然后再和每一个配料做组合。
（3）三进制枚举。同二进制枚举，就看当前位是0、1还是2
"""


class Solution:
    @staticmethod
    def closestCost(baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        # l = set(baseCosts)
        # for i in toppingCosts:
        #     for j in list(l):
        #         if j > target: continue
        #         if j == target: return target
        #         l.add(j + i)
        #         l.add(j + i + i)

        # l = sorted(list(l))
        # if target <= l[0]:
        #     return l[0]
        # elif target >= l[-1]:
        #     return l[-1]
        # else:
        #     i = bisect_left(l, target)
        #     if l[i] == target: return target
        #     if target - l[i - 1] > l[i] - target:
        #         return l[i]
        #     return l[i - 1]

        # n, m, ans, Min = len(baseCosts), len(toppingCosts), 0, 0x3f3f3f3f
        # g = []

        # def dfs(u: int, v: int) -> None:
        #     if v == m:
        #         g.append(u)
        #         return
        #     dfs(u, v+1)
        #     dfs(u+toppingCosts[v], v+1)
        #     dfs(u+toppingCosts[v]*2, v+1)

        # for e in baseCosts:
        #     dfs(e, 0)
        # g.sort()
        # for e in g:
        #     if abs(e-target) < Min:
        #         Min = abs(e-target)
        #         ans = e
        # return ans

        m = len(toppingCosts)
        items = []
        for i in range(3 ** m):
            cur = 0
            for j in range(m):
                cur += toppingCosts[j] * (i % 3)
                i //= 3
            items.append(cur)
        res, d = -1, float("inf")
        for b in baseCosts:
            for t in items:
                tmp = b + t
                td = abs(tmp - target)
                if td < d:
                    res, d = tmp, td
                elif td == d and tmp < res:
                    res = tmp
        return res

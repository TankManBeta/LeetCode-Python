# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/12/5 13:41
"""
from collections import deque
from itertools import accumulate
from typing import List

"""
你有一辆货运卡车，你需要用这一辆车把一些箱子从仓库运送到码头。这辆卡车每次运输有 箱子数目的限制 和 总重量的限制 。
给你一个箱子数组 boxes 和三个整数 portsCount, maxBoxes 和 maxWeight ，其中 boxes[i] = [ports​​i​, weighti] 。
    ports​​i 表示第 i 个箱子需要送达的码头， weightsi 是第 i 个箱子的重量。
    portsCount 是码头的数目。
    maxBoxes 和 maxWeight 分别是卡车每趟运输箱子数目和重量的限制。
箱子需要按照 数组顺序 运输，同时每次运输需要遵循以下步骤：
    卡车从 boxes 队列中按顺序取出若干个箱子，但不能违反 maxBoxes 和 maxWeight 限制。
    对于在卡车上的箱子，我们需要 按顺序 处理它们，卡车会通过 一趟行程 将最前面的箱子送到目的地码头并卸货。
    如果卡车已经在对应的码头，那么不需要 额外行程 ，箱子也会立马被卸货。
    卡车上所有箱子都被卸货后，卡车需要 一趟行程 回到仓库，从箱子队列里再取出一些箱子。
卡车在将所有箱子运输并卸货后，最后必须回到仓库。
请你返回将所有箱子送到相应码头的 最少行程 次数。

示例 1：
输入：boxes = [[1,1],[2,1],[1,1]], portsCount = 2, maxBoxes = 3, maxWeight = 3
输出：4
解释：最优策略如下：
- 卡车将所有箱子装上车，到达码头 1 ，然后去码头 2 ，然后再回到码头 1 ，最后回到仓库，总共需要 4 趟行程。
所以总行程数为 4 。
注意到第一个和第三个箱子不能同时被卸货，因为箱子需要按顺序处理（也就是第二个箱子需要先被送到码头 2 ，然后才能处理第三个箱子）。

示例 2：
输入：boxes = [[1,2],[3,3],[3,1],[3,1],[2,4]], portsCount = 3, maxBoxes = 3, maxWeight = 6
输出：6
解释：最优策略如下：
- 卡车首先运输第一个箱子，到达码头 1 ，然后回到仓库，总共 2 趟行程。
- 卡车运输第二、第三、第四个箱子，到达码头 3 ，然后回到仓库，总共 2 趟行程。
- 卡车运输第五个箱子，到达码头 3 ，回到仓库，总共 2 趟行程。
总行程数为 2 + 2 + 2 = 6 。

示例 3：
输入：boxes = [[1,4],[1,2],[2,1],[2,1],[3,2],[3,4]], portsCount = 3, maxBoxes = 6, maxWeight = 7
输出：6
解释：最优策略如下：
- 卡车运输第一和第二个箱子，到达码头 1 ，然后回到仓库，总共 2 趟行程。
- 卡车运输第三和第四个箱子，到达码头 2 ，然后回到仓库，总共 2 趟行程。
- 卡车运输第五和第六个箱子，到达码头 3 ，然后回到仓库，总共 2 趟行程。
总行程数为 2 + 2 + 2 = 6 。

示例 4：
输入：boxes = [[2,4],[2,5],[3,1],[3,2],[3,7],[3,1],[4,4],[1,3],[5,2]], portsCount = 5, maxBoxes = 5, maxWeight = 7
输出：14
解释：最优策略如下：
- 卡车运输第一个箱子，到达码头 2 ，然后回到仓库，总共 2 趟行程。
- 卡车运输第二个箱子，到达码头 2 ，然后回到仓库，总共 2 趟行程。
- 卡车运输第三和第四个箱子，到达码头 3 ，然后回到仓库，总共 2 趟行程。
- 卡车运输第五个箱子，到达码头 3 ，然后回到仓库，总共 2 趟行程。
- 卡车运输第六和第七个箱子，到达码头 3 ，然后去码头 4 ，然后回到仓库，总共 3 趟行程。
- 卡车运输第八和第九个箱子，到达码头 1 ，然后去码头 5 ，然后回到仓库，总共 3 趟行程。
总行程数为 2 + 2 + 2 + 2 + 3 + 3 = 14 。
"""
"""
思路：
（1）动态规划，f[i]表示将前i个送到对应仓库的最小的行程数，所以最后返回f[n]即可。箱子需要按数组顺序运输，每一次运输，卡车会按
顺序取出连续的几个箱子，然后依次送往对应的码头，全部送达之后，又回到了仓库。因此，我们可以枚举上一次运输的最后一个箱子的编号j，
那么f[i]就可以从f[j]转移而来，转移的时候，我们需要考虑以下几个问题：从f[j]转移过来的时候，卡车上的箱子数量不能超过maxBoxes；
从f[j]转移过来的时候，卡车上的箱子总重量不能超过maxWeight。maxBoxes的约束可以通过限制查找范围来约束；maxWeight的约束可以通过
使用前缀和数组计算差值来约束。状态转移方程为：f[i] = min(f[i], f[j] + cs[i - 1] - cs[j] + 2)，主要是看第i个和第j个之间有多少
不相邻的码头要去
（2）思路（1）会超时，所以我们考虑使用单调队列来维护f[j]-cs[j]的最小值。
"""


class Solution:
    def boxDelivering(self, boxes: List[List[int]], portsCount: int, maxBoxes: int, maxWeight: int) -> int:
        # n = len(boxes)
        # ws = list(accumulate((box[1] for box in boxes), initial=0))
        # c = [int(a != b) for a, b in pairwise(box[0] for box in boxes)]
        # cs = list(accumulate(c, initial=0))
        # f = [inf] * (n + 1)
        # f[0] = 0
        # for i in range(1, n + 1):
        #     for j in range(max(0, i - maxBoxes), i):
        #         if ws[i] - ws[j] <= maxWeight:
        #             f[i] = min(f[i], f[j] + cs[i - 1] - cs[j] + 2)
        # return f[n]

        n = len(boxes)
        ws = list(accumulate((box[1] for box in boxes), initial=0))
        c = [int(a != b) for a, b in pairwise(box[0] for box in boxes)]
        cs = list(accumulate(c, initial=0))
        f = [0] * (n + 1)
        q = deque([0])
        for i in range(1, n + 1):
            while q and (i - q[0] > maxBoxes or ws[i] - ws[q[0]] > maxWeight):
                q.popleft()
            if q:
                f[i] = cs[i - 1] + f[q[0]] - cs[q[0]] + 2
            if i < n:
                while q and f[q[-1]] - cs[q[-1]] >= f[i] - cs[i]:
                    q.pop()
                q.append(i)
        return f[n]
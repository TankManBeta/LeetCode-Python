# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/12/10 16:46
"""
from typing import List

"""
给你 n 个长方体 cuboids ，其中第 i 个长方体的长宽高表示为 cuboids[i] = [widthi, lengthi, heighti]（下标从 0 开始）。
请你从 cuboids 选出一个 子集 ，并将它们堆叠起来。
如果 widthi <= widthj 且 lengthi <= lengthj 且 heighti <= heightj ，你就可以将长方体 i 堆叠在长方体 j 上。
你可以通过旋转把长方体的长宽高重新排列，以将它放在另一个长方体上。
返回 堆叠长方体 cuboids 可以得到的 最大高度 。

示例 1：
输入：cuboids = [[50,45,20],[95,37,53],[45,23,12]]
输出：190
解释：
第 1 个长方体放在底部，53x37 的一面朝下，高度为 95 。
第 0 个长方体放在中间，45x20 的一面朝下，高度为 50 。
第 2 个长方体放在上面，23x12 的一面朝下，高度为 45 。
总高度是 95 + 50 + 45 = 190 。

示例 2：
输入：cuboids = [[38,25,45],[76,35,3]]
输出：76
解释：
无法将任何长方体放在另一个上面。
选择第 1 个长方体然后旋转它，使 35x3 的一面朝下，其高度为 76 。

示例 3：
输入：cuboids = [[7,11,17],[7,17,11],[11,7,17],[11,17,7],[17,7,11],[17,11,7]]
输出：102
解释：
重新排列长方体后，可以看到所有长方体的尺寸都相同。
你可以把 11x7 的一面朝下，这样它们的高度就是 17 。
堆叠长方体的最大高度为 6 * 17 = 102 。
"""
"""
思路：使用dp，将长方体按照长宽高进行排序，并按照定义进行叠加。先证明如果w1≤w2，l1≤l2，h1≤h2，可以堆叠，根据定义可知，显然成立。
然后再证明两个长方体可以堆叠必须满足w1≤w2，l1≤l2，h1≤h2，这里可以采用逆否命题进行证明，即证明w1>w2或l1>l2或h1>h2的条件下不能
堆叠即可。举个例子若w1>w2，w1≤l1≤h1，w2≤l2≤h2，则h1≥l1≥w1>w2，则w2没有可以匹配的边，不满足堆叠的条件。
"""


class Solution:
    @staticmethod
    def maxHeight(cuboids: List[List[int]]) -> int:
        for c in cuboids:
            c.sort()
        cuboids.sort()
        f = [x[2] for x in cuboids]
        for i, (_, l2, h2) in enumerate(cuboids):
            for j, (_, l1, h1) in enumerate(cuboids[:i]):
                if l1 <= l2 and h1 <= h2:
                    f[i] = max(f[i], f[j] + h2)
        return max(f)

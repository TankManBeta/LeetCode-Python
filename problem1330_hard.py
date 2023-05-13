# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/5/12 9:59
"""
from math import inf
from typing import List

"""
给你一个整数数组 nums 。「数组值」定义为所有满足 0 <= i < nums.length-1 的 |nums[i]-nums[i+1]| 的和。
你可以选择给定数组的任意子数组，并将该子数组翻转。但你只能执行这个操作 一次 。
请你找到可行的最大 数组值 。 

示例 1：
输入：nums = [2,3,1,5,4]
输出：10
解释：通过翻转子数组 [3,1,5] ，数组变成 [2,5,1,3,4] ，数组值为 10 。

示例 2：
输入：nums = [2,4,9,24,2,1,10]
输出：68
"""
"""
思路：分类讨论，一共有如下四种情况
    不翻转子数组
    翻转子数组，且子数组“包含”第一个元素
    翻转子数组，且子数组“包含”最后一个元素
    翻转子数组，且子数组“不包含”第一个元素和最后一个元素
我们记不翻转子数组时的数组值为 s，此时有 s=∑_{i=0}^{n−2}∣a_{i}−a_{i+1}∣。我们可以将答案 ans 初始化为 s。
如果翻转子数组，且子数组包含第一个元素，我们可以枚举翻转的子数组的最后一个元素 a_{i}，其中 0≤i<n−1，此时有 
ans=max(ans,s+∣a_{0}−a_{i+1}∣−∣a_{i}−a{i+1}∣)。
如果翻转子数组，且子数组包含最后一个元素，我们可以枚举翻转的子数组的第一个元素 a_{i+1}，其中 0≤i<n−1，此时有 
ans=max(ans,s+∣a_{n−1}−a_{i}∣−∣a_{i}−a_{i+1}∣)。
如果翻转子数组，且子数组不包含第一个元素和最后一个元素，我们将数组任意两个相邻元素视为一个点对 (x,y)，记翻转的第一个元素为 y1，
其左侧相邻元素为 x1 ；翻转的最后一个元素为 x2，其右侧相邻元素为 y2 。此时相比较于不翻转子数组，数组值的变化量为 
∣x1−x2∣+∣y1−y2∣−∣x1−y1∣−∣x2−y2∣，其中，前两项可以表示为：∣x1−x2∣+∣y1−y2∣=max {(x1+y1)−(x2+y2),(x1-y1)−(x2-y2),(-x1+y1)−(-x2+y2),
(-x1-y1)−(-x2-y2)}。那么数组值变化量为：∣x1−x2∣+∣y1−y2∣−∣x1−y1∣−∣x2−y2∣=max{(x1+y1)−∣x1−y1∣−((x2+y2)+∣x2−y2∣),(x1-y1)−∣x1−y1∣−((x2-y2)+∣x2−y2∣),
(-x1+y1)−∣x1−y1∣−((-x2+y2)+∣x2−y2∣),(-x1-y1)−∣x1−y1∣−((-x2-y2)+∣x2−y2∣)}。因此，我们只要求出 k1×x+k2×y 的最大值 mx，
其中 k1,k2∈{−1,1}，以及对应的 ∣x−y∣ 的最小值 mi，那么数组值变化量的最大值为 mx−mi。答案为 ans=max(ans,s+max(0,mx−mi))。
"""


class Solution:
    @staticmethod
    def maxValueAfterReverse(nums: List[int]) -> int:
        ans = s = sum(abs(x - y) for x, y in pairwise(nums))
        for x, y in pairwise(nums):
            ans = max(ans, s + abs(nums[0] - y) - abs(x - y))
            ans = max(ans, s + abs(nums[-1] - x) - abs(x - y))
        for k1, k2 in pairwise((1, -1, -1, 1, 1)):
            mx, mi = -inf, inf
            for x, y in pairwise(nums):
                a = k1 * x + k2 * y
                b = abs(x - y)
                mx = max(mx, a - b)
                mi = min(mi, a + b)
            ans = max(ans, s + max(mx - mi, 0))
        return ans

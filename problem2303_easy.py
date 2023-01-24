# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/1/23 17:30
"""
from typing import List

"""
给你一个下标从 0 开始的二维整数数组 brackets ，其中 brackets[i] = [upperi, percenti] ，表示第 i 个税级的上限是 upperi ，
征收的税率为 percenti 。税级按上限 从低到高排序（在满足 0 < i < brackets.length 的前提下，upperi-1 < upperi）。
税款计算方式如下：
    不超过 upper0 的收入按税率 percent0 缴纳
    接着 upper1 - upper0 的部分按税率 percent1 缴纳
    然后 upper2 - upper1 的部分按税率 percent2 缴纳
    以此类推
给你一个整数 income 表示你的总收入。返回你需要缴纳的税款总额。与标准答案误差不超 10-5 的结果将被视作正确答案。

示例 1：
输入：brackets = [[3,50],[7,10],[12,25]], income = 10
输出：2.65000
解释：
前 $3 的税率为 50% 。需要支付税款 $3 * 50% = $1.50 。
接下来 $7 - $3 = $4 的税率为 10% 。需要支付税款 $4 * 10% = $0.40 。
最后 $10 - $7 = $3 的税率为 25% 。需要支付税款 $3 * 25% = $0.75 。
需要支付的税款总计 $1.50 + $0.40 + $0.75 = $2.65 。

示例 2：
输入：brackets = [[1,0],[4,25],[5,50]], income = 2
输出：0.25000
解释：
前 $1 的税率为 0% 。需要支付税款 $1 * 0% = $0 。
剩下 $1 的税率为 25% 。需要支付税款 $1 * 25% = $0.25 。
需要支付的税款总计 $0 + $0.25 = $0.25 。

示例 3：
输入：brackets = [[2,50]], income = 0
输出：0.00000
解释：
没有收入，无需纳税，需要支付的税款总计 $0 。
"""
"""
思路：在最前面添个[0,0]，然后模拟即可
"""


class Solution:
    @staticmethod
    def calculateTax(brackets: List[List[int]], income: int) -> float:
        ans = 0.0
        brackets = [[0, 0]] + brackets
        n = len(brackets)
        for i in range(1, n):
            if income > brackets[i][0]:
                ans += (brackets[i][0] - brackets[i - 1][0]) * brackets[i][1] / 100
            else:
                ans += (income - brackets[i - 1][0]) * brackets[i][1] / 100
                return ans

# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/5/18 21:21
"""
"""
几乎每一个人都用 乘法表。但是你能在乘法表中快速找到第k小的数字吗？
给定高度m 、宽度n 的一张 m * n的乘法表，以及正整数k，你需要返回表中第k 小的数字。

输入: m = 3, n = 3, k = 5
输出: 3
解释: 
乘法表:
1	2	3
2	4	6
3	6	9
第5小的数字是 3 (1, 2, 2, 3, 3).

输入: m = 2, n = 3, k = 6
输出: 6
解释: 
乘法表:
1	2	3
2	4	6
第6小的数字是 6 (1, 2, 2, 3, 4, 6).
"""
"""
思路：初始化 left = 1, right = m*n, 进行二分搜索找到 k−th 数字。我们使用自定义的count函数来计算当前矩阵中小于等于mid值的数字
数量。(具体步骤请看动图) 我们采用从左下角开始搜索的二分策略。当二分搜索结束后，如果当前count < k，那么我们应该调整left值将其
变大使得新的mid能逼近k, 及left = mid + 1反之count >= k，那么我们应该调整right值将其变小使得新的mid也能逼近k, 及right = mid
"""


class Solution(object):
    # def findKthNumber(self, m, n, k):
    #     """
    #     :type m: int
    #     :type n: int
    #     :type k: int
    #     :rtype: int
    #     """

    def cnt(self, mid, m, n):
        ret, i, j = 0, m, 1
        while i >= 1 and j <= n:
            if i*j <= mid:
                ret += i
                j += 1
            else:
                i -= 1
        return ret

    def findKthNumber(self, m, n, k):
        l, r = 1, m*n
        while l < r:
            mid = (l+r) >> 1
            if self.cnt(mid, m, n) < k:
                l = mid+1
            else:
                r = mid
        return l

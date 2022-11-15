# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/11/14 21:33
"""
"""
你是产品经理，目前正在带领一个团队开发新的产品。不幸的是，你的产品的最新版本没有通过质量检测。
由于每个版本都是基于之前的版本开发的，所以错误的版本之后的所有版本都是错的。
假设你有 n 个版本 [1, 2, ..., n]，你想找出导致之后所有版本出错的第一个错误的版本。
你可以通过调用 bool isBadVersion(version) 接口来判断版本号 version 是否在单元测试中出错。
实现一个函数来查找第一个错误的版本。你应该尽量减少对调用 API 的次数。

示例 1：
输入：n = 5, bad = 4
输出：4
解释：
调用 isBadVersion(3) -> false 
调用 isBadVersion(5) -> true 
调用 isBadVersion(4) -> true
所以，4 是第一个错误的版本。

示例 2：
输入：n = 1, bad = 1
输出：1
"""
"""
思路：二分查找
"""


# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    pass


class Solution:
    def firstBadVersion(self, n: int) -> int:
        i, j = 1, n
        while i <= j:
            # 向下取整除法计算中点 m
            m = i + (j-i) // 2
            # 若 m 是错误版本，则最后一个正确版本一定在闭区间 [i, m - 1]
            if isBadVersion(m):
                j = m - 1
            # 若 m 是正确版本，则首个错误版本一定在闭区间 [m + 1, j]
            else:
                i = m + 1
        # i 指向首个错误版本，j 指向最后一个正确版本
        return i

# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/1/30 15:59
"""
"""
给你一个非负整数 x ，计算并返回 x 的 算术平方根 。
由于返回类型是整数，结果只保留 整数部分 ，小数部分将被 舍去 。
注意：不允许使用任何内置指数函数和算符，例如 pow(x, 0.5) 或者 x ** 0.5 。

输入：x = 4
输出：2

输入：x = 8
输出：2
解释：8 的算术平方根是 2.82842..., 由于返回类型是整数，小数部分将被舍去。
"""
"""
思路：
（1）二分查找，找mid*mid<=x即可
（2）牛顿迭代法，求y=f(x)=x^2-C的零点，我们选择x0=C为初始值，求得在x0处的切线与x轴的交点x1为新的x0，循环直到两次误差小于1e-7
"""


class Solution(object):
    @staticmethod
    def my_sqrt(x):
        """
        :type x: int
        :rtype: int
        """
        # left = 0
        # right = x
        # ans = -1
        # while left <= right:
        #     mid = (left + right) // 2
        #     if mid * mid <= x:
        #         ans = mid
        #         left = mid + 1
        #     else:
        #         right = mid - 1
        # return ans

        if x == 0:
            return 0
        c, x0 = float(x), float(x)
        while True:
            xi = 0.5 * (x0 + c / x0)
            if abs(x0 - xi) < 1e-7:
                break
            x0 = xi
        return int(x0)

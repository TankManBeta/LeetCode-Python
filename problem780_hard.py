# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/4/9 14:08
"""
"""
给定四个整数 sx , sy ，tx 和 ty，如果通过一系列的转换可以从起点 (sx, sy) 到达终点 (tx, ty)，则返回 true，否则返回 false。
从点 (x, y) 可以转换到 (x, x+y)  或者 (x+y, y)。

输入: sx = 1, sy = 1, tx = 3, ty = 5
输出: true
解释:
可以通过以下一系列转换从起点转换到终点：
(1, 1) -> (1, 2)
(1, 2) -> (3, 2)
(3, 2) -> (3, 5)

输入: sx = 1, sy = 1, tx = 2, ty = 2 
输出: false

输入: sx = 1, sy = 1, tx = 1, ty = 1 
输出: true
"""
"""
思路：反向减，在某次反向转换中，如果有tx<ty，我们会将(tx,ty)转换为(tx,ty−tx)，若相减完仍有tx<ty−tx，该操作会继续进行，得到
(tx,ty−2∗tx)，直到不满足tx<ty−k∗tx，其中k为转换次数。即对于一般性的情况而言，(tx,ty) 中的较大数会一直消减到「与较小数的余数」
为止。
"""


class Solution(object):
    @staticmethod
    def reachingPoints(sx, sy, tx, ty):
        """
        :type sx: int
        :type sy: int
        :type tx: int
        :type ty: int
        :rtype: bool
        """
        while sx < tx and sy < ty:
            if tx > ty:
                tx %= ty
            else:
                ty %= tx
        if sx > tx or sy > ty:
            return False
        return (ty - sy) % tx == 0 if tx == sx else (tx - sx) % ty == 0

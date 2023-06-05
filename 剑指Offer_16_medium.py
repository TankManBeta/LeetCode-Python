# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/6/4 10:17
"""
"""
实现 pow(x, n) ，即计算 x 的 n 次幂函数（即，xn）。不得使用库函数，同时不需要考虑大数问题。

示例 1：
输入：x = 2.00000, n = 10
输出：1024.00000

示例 2：
输入：x = 2.10000, n = 3
输出：9.26100

示例 3：
输入：x = 2.00000, n = -2
输出：0.25000
解释：2-2 = 1/22 = 1/4 = 0.25
"""
"""
思路：
（1）当我们要计算 x**n 时，我们可以先递归地计算出 y=x**⌊n/2⌋，其中 ⌊a⌋ 表示对 a 进行下取整；根据递归计算的结果，如果 n 为偶数，
那么 x**n=y**2 ；如果 n 为奇数，那么 x**n=y**2×x；递归的边界为 n=0，任意数的 0 次方均为 1。
（2）当 x=0 时：直接返回 0 （避免后续 x=1/x 操作报错）。初始化 res=1 ；n<0 时：把问题转化至 n≥0 的范围内，即执行 x=1/x ，n=−n ；
循环计算：当 n=0 时跳出；当 n&1=1 时：将当前 x 乘入 res （即 res∗=x ）；执行 x=x**2（即 x∗=x ）；执行 n 右移一位（即 n>>=1）。
返回 res 。如果整数 n 的二进制拆分为n=2**i0+2**i1+⋯+2**ik，那么x**n=x**2**i0×x**2**i1×⋯×x**2**ik。这样一来，我们从 x 开始
不断地进行平方，得到 x**2,x**4,x**8,x**16,⋯，如果 n 的第 k 个（从右往左，从 0 开始计数）二进制位为 1，那么我们就将对应的贡献 
x**2**k 计入答案。
"""


class Solution:
    @staticmethod
    def myPow(x: float, n: int) -> float:
        # def quickMul(N):
        #     if N == 0:
        #         return 1.0
        #     y = quickMul(N // 2)
        #     return y * y if N % 2 == 0 else y * y * x

        # return quickMul(n) if n >= 0 else 1.0 / quickMul(-n)

        if x == 0:
            return 0
        res = 1
        if n < 0:
            x, n = 1 / x, -n
        while n:
            if n & 1:
                res *= x
            x *= x
            n >>= 1
        return res

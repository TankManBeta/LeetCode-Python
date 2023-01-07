# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/1/6 14:36
"""
"""
给你一个正整数 num ，请你统计并返回 小于或等于 num 且各位数字之和为 偶数 的正整数的数目。
正整数的 各位数字之和 是其所有位上的对应数字相加的结果。

示例 1：
输入：num = 4
输出：2
解释：
只有 2 和 4 满足小于等于 4 且各位数字之和为偶数。
    
示例 2：
输入：num = 30
输出：14
解释：
只有 14 个整数满足小于等于 30 且各位数字之和为偶数，分别是： 2、4、6、8、11、13、15、17、19、20、22、24、26 和 28 。
"""
"""
思路：
（1）暴力枚举
（2）先看有多少个10，然后看剩下的几个数中有几个数位和为偶数的
（3）找规律，根据num奇偶来判断
"""


class Solution:
    @staticmethod
    def countEven(num: int) -> int:
        def is_even(n):
            count = 0
            while n:
                count += n % 10
                n //= 10
            return count % 2 == 0

        # full = num // 10 * 5
        # ans = full
        # if num % 10 == 0:
        #     if is_even(num):
        #         return ans
        #     else:
        #         return ans-1
        # else:
        #     for i in range(num//10*10, num+1):
        #         if is_even(i):
        #             ans += 1
        #     return ans-1

        if is_even(num):
            return num // 2
        else:
            return (num - 1) // 2

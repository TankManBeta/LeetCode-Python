# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/3/26 15:10
"""
"""
给定整数 n ，返回 所有小于非负整数 n 的质数的数量 。

输入：n = 10
输出：4
解释：小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。

输入：n = 0
输出：0

输入：n = 1
输出：0
"""
"""
思路：
（1）暴力（超时）：直接判断每个数是不是素数
（2）埃氏筛：每次标记当前素数的倍数，注意从x*x开始标记，因为那些2*x，3*x已经在之前被素数2，3标记过。复杂度O(log(log(n)))
（3）线性筛：多维护一个primes数组，对于当前的数字x，如果x是素数，就添加到primes中，然后标记对于primes中每一个素数prime，标记prime*x为合数，
直到x%prime为0，为什么在这个条件下停止标记，假设当前数字为x，能够整除的素数为primes[i]，对于下一个x*primes[i+1]，它一定会在x/primes[i]*
primes[i+1]被标记，所以我们做到了在最小质因数下标记。
"""


class Solution(object):
    @staticmethod
    def countPrimes(n):
        """
        :type n: int
        :rtype: int
        """
        # def is_prime(number):
        #     i = 2
        #     while(i*i<=number):
        #         if number%i == 0:
        #             return False
        #         i += 1
        #     return True
        # ans = 0
        # for num in range(2, n):
        #     ans += is_prime(num)
        # return ans

        # 埃氏筛
        is_prime = [1]*n
        ans = 0
        for i in range(2, n):
            if is_prime[i] == 1:
                ans += 1
                if i*i < n:
                    for j in range(i * i, n, i):
                        is_prime[j] = 0
        return ans

        # 线性筛
        # is_prime = [1]*n
        # primes = []
        # count = 0
        # for i in range(2, n):
        #     if is_prime[i] == 1:
        #         primes.append(i)
        #         count += 1
        #     for prime in primes:
        #         if i*prime < n:
        #             is_prime[i*prime] = 0
        #             if i%prime == 0:
        #                 break
        #         else:
        #             break
        # return count

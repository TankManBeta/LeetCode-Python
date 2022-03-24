# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/3/23 13:46
"""
"""
给定整数 n 和 k，返回  [1, n] 中字典序第 k 小的数字。

输入: n = 13, k = 2
输出: 10
解释: 字典序的排列是 [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]，所以第二小的数字是 10。

输入: n = 1, k = 1
输出: 1
"""
"""
思路：算出以当前前缀prefix开头并且不大于n的数字的个数cnt，如果cnt<k，说明它不在以prefix为前缀的数字中，prefix+=1，继续计算；
如果cnt>=k，则说明在当前为前缀的数字当中prefix*=10
"""


class Solution(object):
    @staticmethod
    def findKthNumber(n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """

        def get_count(prefix, limit):
            count = 0
            next_prefix = prefix + 1
            while prefix <= limit:
                count += min(limit + 1, next_prefix) - prefix
                prefix *= 10
                next_prefix *= 10
            return count

        ans = 1
        while k > 1:
            cnt = get_count(ans, n)
            if cnt < k:
                ans += 1
                k -= cnt
            else:
                ans *= 10
                k -= 1
        return ans

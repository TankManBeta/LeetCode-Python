# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/1/10 22:58
"""
"""
有一个需要密码才能打开的保险箱。密码是 n 位数, 密码的每一位是 k 位序列 0, 1, ..., k-1 中的一个 。
你可以随意输入密码，保险箱会自动记住最后 n 位输入，如果匹配，则能够打开保险箱。
举个例子，假设密码是 "345"，你可以输入 "012345" 来打开它，只是你输入了 6 个字符.
请返回一个能打开保险箱的最短字符串。

示例1:
输入: n = 1, k = 2
输出: "01"
说明: "10"也可以打开保险箱。

示例2:
输入: n = 2, k = 2
输出: "00110"
说明: "01100", "10011", "11001" 也能打开保险箱。
"""
"""
思路：题目的目的是找到一个最短字符串，包含密码的所有可能。也就是找到一个欧拉回路，
"""


class Solution:
    @staticmethod
    def crackSafe(n: int, k: int) -> str:
        seen = set()
        ans = list()
        highest = 10 ** (n - 1)

        def dfs(node: int):
            # 每个点对应的k条边
            for x in range(k):
                # 边的编号
                nei = node * 10 + x
                # 未访问过
                if nei not in seen:
                    seen.add(nei)
                    # 去掉第一位为结点编号
                    dfs(nei % highest)
                    # 添加最后一个数字
                    ans.append(str(x))

        dfs(0)
        return "".join(ans) + "0" * (n - 1)

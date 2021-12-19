# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2021/12/19 19:56
"""
"""
在一个小镇里，按从 1 到 n 为 n 个人进行编号。传言称，这些人中有一个是小镇上的秘密法官。
如果小镇的法官真的存在，那么：
小镇的法官不相信任何人。
每个人（除了小镇法官外）都信任小镇的法官。
只有一个人同时满足条件 1 和条件 2 。
给定数组 trust，该数组由信任对 trust[i] = [a, b] 组成，表示编号为 a 的人信任编号为 b 的人。
如果小镇存在秘密法官并且可以确定他的身份，请返回该法官的编号。否则，返回 -1。

输入：n = 2, trust = [[1,2]]
输出：2

输入：n = 3, trust = [[1,3],[2,3]]
输出：3

输入：n = 3, trust = [[1,3],[2,3],[3,1]]
输出：-1

输入：n = 3, trust = [[1,2],[2,3]]
输出：-1

输入：n = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
输出：3
"""
"""
思路：对于trust里每一个，相信别人的变成1，被相信的人+1，返回不相信别人的并且被其他人相信的人
"""


class Solution(object):
    @staticmethod
    def find_judge(n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        result_list = [[0, 0] for _ in range(n)]
        for evidence in trust:
            result_list[evidence[0]-1][0] = 1
            result_list[evidence[1]-1][1] += 1
        for key, value in enumerate(result_list):
            if value[0] == 0 and value[1] == n-1:
                return key+1
        return -1

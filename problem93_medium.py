# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/2/18 11:21
"""
"""
有效 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。
例如："0.1.2.201" 和 "192.168.1.1" 是 有效 IP 地址，但是 "0.011.255.245"、"192.168.1.312" 和 "192.168@1.1" 是无效IP 地址。
给定一个只包含数字的字符串 s ，用以表示一个 IP 地址，返回所有可能的有效 IP 地址，这些地址可以通过在 s 中插入 '.' 来形成。
你不能重新排序或删除 s 中的任何数字。你可以按任何顺序返回答案。

输入：s = "0000"
输出：["0.0.0.0"]

输入：s = "101023"
输出：["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
"""
"""
思路：dfs，注意剪枝即可
"""


class Solution(object):
    @staticmethod
    def restore_ip_addresses(s):
        """
        :type s: str
        :rtype: List[str]
        """
        m = len(s)
        if m < 4:
            return []
        res = []
        temp = []

        def dfs(k, start):
            if k == 4:
                if start == m:
                    res.append('.'.join(temp))
                return
            for i in range(1, 4):
                if start+i-1 >= m:
                    return
                if i != 1 and s[start] == '0':
                    return
                temp_s = s[start:start+i]
                if 0 <= int(temp_s) <= 255:
                    temp.append(temp_s)
                    dfs(k+1, start+i)
                    temp.pop()
        dfs(0, 0)
        return res

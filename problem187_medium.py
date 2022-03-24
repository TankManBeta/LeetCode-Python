# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/3/23 10:53
"""
"""
DNA序列 由一系列核苷酸组成，缩写为 'A', 'C', 'G' 和 'T'.。
例如，"ACGAATTCCG" 是一个 DNA序列 。
在研究 DNA 时，识别 DNA 中的重复序列非常有用。
给定一个表示 DNA序列 的字符串 s ，返回所有在 DNA 分子中出现不止一次的 长度为 10 的序列(子字符串)。你可以按 任意顺序 返回答案。

输入：s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
输出：["AAAAACCCCC","CCCCCAAAAA"]

输入：s = "AAAAAAAAAAAAA"
输出：["AAAAAAAAAA"]
"""
"""
思路：
（1）哈希表记录每一个长度为10的字符串出现的次数，只有两次的才加入ans
（2）一个字符用2比特表示，然后算字串的值作为key放入到哈希表中，字符每次取一个，但是x要左移两个比特
"""


class Solution(object):
    @staticmethod
    def findRepeatedDnaSequences(s):
        """
        :type s: str
        :rtype: List[str]
        """
        # n = len(s)
        # hash_dict = {}
        # ans = []
        # if n <= 10:
        #     return ans
        # for i in range(0, n-9):
        #     hash_dict[s[i:i+10]] = hash_dict.get(s[i:i+10], 0) + 1
        #     if hash_dict[s[i:i+10]] == 2:
        #         ans.append(s[i:i+10])
        # return ans

        n = len(s)
        hash_dict = {}
        L = 10
        bin_map = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        ans = []
        if n <= 10:
            return ans

        # 前9个字符
        x = 0
        for ch in s[:10 - 1]:
            x = (x << 2) | bin_map[ch]

        for i in range(n - L + 1):
            # 只考虑低20位比特
            x = ((x << 2) | bin_map[s[i + L - 1]]) & ((1 << (L * 2)) - 1)
            hash_dict[x] = hash_dict.get(x, 0) + 1
            if hash_dict[x] == 2:
                ans.append(s[i: i + L])
        return ans

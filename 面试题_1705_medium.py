# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/3/11 14:27
"""
from typing import List

"""
给定一个放有字母和数字的数组，找到最长的子数组，且包含的字母和数字的个数相同。
返回该子数组，若存在多个最长子数组，返回左端点下标值最小的子数组。若不存在这样的数组，返回一个空数组。

示例 1:
输入: ["A","1","B","C","D","2","3","4","E","5","F","G","6","7","H","I","J","K","L","M"]
输出: ["A","1","B","C","D","2","3","4","E","5","F","G","6","7"]

示例 2:
输入: ["A","A"]
输出: []
"""
"""
思路：前缀和+哈希。和昨天的每日一题优点相似，我们定义字符的贡献为1，非字符的贡献为-1。max_len为结果的最大长度，left为结果的起始
位置，total为前缀和，index为哈希表记录每一个前缀和第一次出现的位置。我们遍历到一个位置，看这个位置的前缀和是否已经出现过，如果
未出现过就添加进哈希表；如果出现过则找出第一次出现的位置记为j，因为两个前缀和相同，所以他们之间夹着的那些数和为0。此时更新看是否
比已有的结果大。
"""


class Solution:
    @staticmethod
    def findLongestSubarray(array: List[str]) -> List[str]:
        max_len = 0
        total = 0
        left = 0
        index = {0: -1}
        for i, item in enumerate(array):
            total += 1 if item.isalpha() else -1
            if total in index:
                already = index[total]
                if i - already > max_len:
                    max_len = i - already
                    left = already + 1
            else:
                index[total] = i
        if max_len == 0:
            return []
        return array[left: left + max_len]

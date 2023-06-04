# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/6/3 11:29
"""
from collections import Counter

"""
如果字符串中的所有字符都相同，那么这个字符串是单字符重复的字符串。
给你一个字符串 text，你只能交换其中两个字符一次或者什么都不做，然后得到一些单字符重复的子串。返回其中最长的子串的长度。 

示例 1：
输入：text = "ababa"
输出：3

示例 2：
输入：text = "aaabaaa"
输出：6

示例 3：
输入：text = "aaabbaaa"
输出：4

示例 4：
输入：text = "aaaaa"
输出：5

示例 5：
输入：text = "abcdef"
输出：1
"""
"""
思路：双指针，我们先用哈希表或数组 cnt 统计字符串 text 中每个字符出现的次数。接下来，我们定义一个指针 i，初始时 i=0。每一次，
我们将指针 j 指向 i，并不断地向右移动 j，直到 j 指向的字符与 i 指向的字符不同，此时我们得到了一个长度为 l=j−i 的子串 text[i..j−1]，
其中所有字符都相同。然后我们跳过指针 j 指向的字符，用指针 k 继续向右移动，直到 k 指向的字符与 i 指向的字符不同，此时我们得到了
一个长度为 r=k−j−1 的子串 text[j+1..k−1]，其中所有字符都相同。那么我们最多通过一次交换操作，可以得到的最长单字符重复子串的长度
为 min(l+r+1,cnt[text[i]])。接下来，我们将指针 i 移动到 j，继续寻找下一个子串。我们取所有满足条件的子串的最大长度即可。之所以
是l+r+1是为了避免"aaabaaaba"这种情况，因为第一个b可以用最后的a代替。
"""


class Solution:
    @staticmethod
    def maxRepOpt1(text: str) -> int:
        cnt = Counter(text)
        n = len(text)
        ans = i = 0
        while i < n:
            j = i
            while j < n and text[j] == text[i]:
                j += 1
            l = j - i
            k = j + 1
            while k < n and text[k] == text[i]:
                k += 1
            r = k - j - 1
            ans = max(ans, min(l + r + 1, cnt[text[i]]))
            i = j
        return ans

# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/3/18 14:17
"""
"""
给你两个字符串 a 和 b ，它们长度相同。请你选择一个下标，将两个字符串都在 相同的下标 分割开。由 a 可以得到两个字符串： aprefix 和 asuffix ，满足 a = aprefix + asuffix ，同理，由 b 可以得到两个字符串 bprefix 和 bsuffix ，满足 b = bprefix + bsuffix 。请你判断 aprefix + bsuffix 或者 bprefix + asuffix 能否构成回文串。

当你将一个字符串 s 分割成 sprefix 和 ssuffix 时， ssuffix 或者 sprefix 可以为空。比方说， s = "abc" 那么 "" + "abc" ， 
"a" + "bc" ， "ab" + "c" 和 "abc" + "" 都是合法分割。
如果 能构成回文字符串 ，那么请返回 true，否则返回 false 。
注意， x + y 表示连接字符串 x 和 y 。

示例 1：
输入：a = "x", b = "y"
输出：true
解释：如果 a 或者 b 是回文串，那么答案一定为 true ，因为你可以如下分割：
aprefix = "", asuffix = "x"
bprefix = "", bsuffix = "y"
那么 aprefix + bsuffix = "" + "y" = "y" 是回文串。

示例 2：
输入：a = "abdef", b = "fecab"
输出：true

示例 3：
输入：a = "ulacfd", b = "jizalu"
输出：true
解释：在下标为 3 处分割：
aprefix = "ula", asuffix = "cfd"
bprefix = "jiz", bsuffix = "alu"
那么 aprefix + bsuffix = "ula" + "alu" = "ulaalu" 是回文串。
"""
"""
思路：我们可以使用双指针，其中一个指针 i 从字符串 a 的头部开始，另一个指针 j 从字符串 b 的尾部开始，如果两个指针指向的字符相等，
那么两个指针同时往中间移动，直到遇到不同的字符或两指针交叉。如果两指针交叉，即 i≥j，说明 prefix 和 suffix 已经可以得到回文串，
返回 true；否则，我们还需要判断 a[i,...j] 或者 b[i,...j] 是否是回文串，若是，返回 true。否则，我们尝试交换两个字符串 a 和 b，
重复上述同样的过程。
"""


class Solution:
    @staticmethod
    def checkPalindromeFormation(a: str, b: str) -> bool:
        def check1(a: str, b: str) -> bool:
            i, j = 0, len(b) - 1
            while i < j and a[i] == b[j]:
                i, j = i + 1, j - 1
            return i >= j or check2(a, i, j) or check2(b, i, j)

        def check2(a: str, i: int, j: int) -> bool:
            return a[i: j + 1] == a[i: j + 1][::-1]

        return check1(a, b) or check1(b, a)

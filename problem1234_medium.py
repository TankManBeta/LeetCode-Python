# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/2/13 19:55
"""
from collections import Counter
from math import inf

"""
有一个只含有 'Q', 'W', 'E', 'R' 四种字符，且长度为 n 的字符串。
假如在该字符串中，这四个字符都恰好出现 n/4 次，那么它就是一个「平衡字符串」。
给你一个这样的字符串 s，请通过「替换一个子串」的方式，使原字符串 s 变成一个「平衡字符串」。
你可以用和「待替换子串」长度相同的 任何 其他字符串来完成替换。
请返回待替换子串的最小可能长度。
如果原字符串自身就是一个平衡字符串，则返回 0。

示例 1：
输入：s = "QWER"
输出：0
解释：s 已经是平衡的了。

示例 2：
输入：s = "QQWE"
输出：1
解释：我们需要把一个 'Q' 替换成 'R'，这样得到的 "RQWE" (或 "QRWE") 是平衡的。

示例 3：
输入：s = "QQQW"
输出：2
解释：我们可以把前面的 "QQ" 替换成 "ER"。 

示例 4：
输入：s = "QQQQ"
输出：3
解释：我们可以替换后 3 个 'Q'，使 s = "QWER"。
"""
"""
思路：这道题的难点是我们要反过来考虑。我们不要考虑要替换子串的相关信息，而需要考虑使得处理要替换子串之外的部分每个字符出现的次数
不能超过n//4。所以我们可以使用滑动窗口，每次枚举右端点，每次遍历到一个字符，则在count中将它的数量减一，然后此时缩小左端点，对于
遇到的每个字符，count中将它的数量加一，以满足最短的要求，最后得出答案即可。
"""


class Solution:
    @staticmethod
    def balancedString(s: str) -> int:
        count = Counter(s)
        n = len(s)
        m = n // 4
        if all(count[x] == m for x in "QWER"):  # 已经符合要求啦
            return 0
        ans, left = inf, 0
        for right, c in enumerate(s):  # 枚举子串右端点
            count[c] -= 1
            while all(count[x] <= m for x in "QWER"):
                ans = min(ans, right - left + 1)
                count[s[left]] += 1
                left += 1  # 缩小子串
        return ans

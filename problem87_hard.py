# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/2/22 18:04
"""
"""
使用下面描述的算法可以扰乱字符串 s 得到字符串 t ：
如果字符串的长度为 1 ，算法停止
如果字符串的长度 > 1 ，执行下述步骤：
    在一个随机下标处将字符串分割成两个非空的子字符串。即，如果已知字符串s，则可以将其分成两个子字符串x和y，且满足 s = x + y 。
    随机决定是要「交换两个子字符串」还是要「保持这两个子字符串的顺序不变」。即，在执行这一步骤之后，s可能是s=x+y或者s=y+x 。
    在 x 和 y 这两个子字符串上继续从步骤 1 开始递归执行此算法。
给你两个 长度相等 的字符串 s1 和 s2，判断 s2 是否是 s1 的扰乱字符串。如果是，返回 true ；否则，返回 false 。

输入：s1 = "great", s2 = "rgeat"
输出：true
解释：s1 上可能发生的一种情形是：
"great" --> "gr/eat" // 在一个随机下标处分割得到两个子字符串
"gr/eat" --> "gr/eat" // 随机决定：「保持这两个子字符串的顺序不变」
"gr/eat" --> "g/r / e/at" // 在子字符串上递归执行此算法。两个子字符串分别在随机下标处进行一轮分割
"g/r / e/at" --> "r/g / e/at" // 随机决定：第一组「交换两个子字符串」，第二组「保持这两个子字符串的顺序不变」
"r/g / e/at" --> "r/g / e/ a/t" // 继续递归执行此算法，将 "at" 分割得到 "a/t"
"r/g / e/ a/t" --> "r/g / e/ a/t" // 随机决定：「保持这两个子字符串的顺序不变」
算法终止，结果字符串和 s2 相同，都是 "rgeat"
这是一种能够扰乱 s1 得到 s2 的情形，可以认为 s2 是 s1 的扰乱字符串，返回 true

输入：s1 = "abcde", s2 = "caebd"
输出：false

输入：s1 = "a", s2 = "a"
输出：true
"""
"""
思路：定义状态表示：f[i][j][k]为s1从i开始，s2从j开始k个字符是否匹配，k为区间大小，即待匹配字符串的长度
转移方程：在这长度为k中，枚举分割点u，看s1在u点分割成两段能否和s2匹配，由于s1在u点分割之后还能交换，因此有两种匹配方式:
f[i][j][u]&&f[i+u][j+u][k-u]（根据状态表示，s1的前u个和s2的前u个匹配，s1的后k-u个和s2的后k-u个匹配）和
f[i][j+k-u][u]&&f[i+u][j][k-u]（s1的前u个和s2的后u个匹配，s1的后k-u个和s2的前k-u个匹配），只要这两种匹配有一种匹配成功，
那么f[i][j]k]=true成立主要区间dp时，先枚举区间大小。
"""


class Solution(object):
    @staticmethod
    def is_scramble(s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        # if len(s1) != len(s2):
        #     return False
        # if s1 == s2:
        #     return True
        # if sorted(s1) != sorted(s2):
        #     return False

        # for i in range(1, len(s1)):
        #     if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]) or \
        #             (self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i])):
        #         return True
        # return False

        if len(s1) != len(s2):
            return False
        n = len(s1)
        f = [[[False]*(n+1) for _ in range(n)] for _ in range(n)]
        for k in range(1, n+1):
            for i in range(n-k+1):
                for j in range(n-k+1):
                    if k == 1:
                        f[i][j][k] = s1[i] == s2[j]
                    else:
                        for u in range(1, k):
                            if (f[i][j][u] and f[i+u][j+u][k-u]) or (f[i][j+k-u][u] and f[i+u][j][k-u]):
                                f[i][j][k] = True
        return f[0][0][-1]

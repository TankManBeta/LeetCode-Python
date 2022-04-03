# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/4/2 23:29
"""
"""
如果一个密码满足下述所有条件，则认为这个密码是强密码：
    由至少 6 个，至多 20 个字符组成。
    至少包含 一个小写 字母，一个大写 字母，和 一个数字 。
    同一字符 不能 连续出现三次 (比如 "...aaa..." 是不允许的, 但是 "...aa...a..." 如果满足其他条件也可以算是强密码)。
给你一个字符串 password ，返回 将 password 修改到满足强密码条件需要的最少修改步数。如果 password 已经是强密码，则返回 0 。
在一步修改操作中，你可以：
    插入一个字符到 password ，
    从 password 中删除一个字符，或
    用另一个字符来替换 password 中的某个字符。

输入：password = "a"
输出：5

输入：password = "aA1"
输出：3

输入：password = "1337C0d3"
输出：0
"""
"""
思路：分类讨论模拟，长度小于6时，需要添加长度到6（添加时可以去除长度为3的情况），同时要满足种类为3的要求，结果就是max(6-n, 3-m)；长度为6-20时，只需要删除三个数字连在一起的情况，同时要满足种类为3的情况；长度大于20时，肯定要删除n-20次，然后通过删除可以减少一部分替换操作，例如3，6，9这种长度的连续子串，删除一个就能减少一次替换操作，想4，7，10这种删除两个才能减少一次替换操作
"""

class Solution(object):
    def strongPasswordChecker(self, password):
        """
        :type password: str
        :rtype: int
        """
        n = len(password)
        a, b, c = 0, 0, 0
        for char in password:
            if 'a' <= char <= 'z':
                a = 1
            elif 'A' <= char <= 'Z':
                b = 1
            elif '0' <= char <= '9':
                c = 1
        m = a + b + c
        if n < 6:
            return max(6-n, 3-m)
        elif n <= 20:
            tot = 0
            i = 0
            while i < n:
                j = i
                while j < n and password[j] == password[i]:
                    j += 1
                l = j - i
                if l >= 3:
                    tot += (l//3)
                i = j
            return max(tot, 3-m)
        else:
            tot = 0
            counts = [0, 0, 0]
            i = 0
            while i<n:
                j = i
                while j < n and password[j] == password[i]:
                    j += 1
                l = j - i
                if l >= 3:
                    tot += l // 3
                    counts[l % 3] += 1
                i = j
            base = n - 20
            cur = base
            for i in range(3):
                if i == 2:
                    counts[i] = tot
                if counts[i] != 0 and cur != 0:
                    t = min(counts[i] * (i + 1), cur)
                    cur -= t
                    tot -= t / (i + 1)
            return base + max(tot, 3 - m)
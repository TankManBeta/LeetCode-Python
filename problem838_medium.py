# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/2/21 10:46
"""
"""
n 张多米诺骨牌排成一行，将每张多米诺骨牌垂直竖立。在开始时，同时把一些多米诺骨牌向左或向右推。
每过一秒，倒向左边的多米诺骨牌会推动其左侧相邻的多米诺骨牌。同样地，倒向右边的多米诺骨牌也会推动竖立在其右侧的相邻多米诺骨牌。
如果一张垂直竖立的多米诺骨牌的两侧同时有多米诺骨牌倒下时，由于受力平衡， 该骨牌仍然保持不变。
就这个问题而言，我们会认为一张正在倒下的多米诺骨牌不会对其它正在倒下或已经倒下的多米诺骨牌施加额外的力。
给你一个字符串 dominoes 表示这一行多米诺骨牌的初始状态，其中：
    dominoes[i] = 'L'，表示第 i 张多米诺骨牌被推向左侧，
    dominoes[i] = 'R'，表示第 i 张多米诺骨牌被推向右侧，
    dominoes[i] = '.'，表示没有推动第 i 张多米诺骨牌。
返回表示最终状态的字符串。

输入：dominoes = "RR.L"
输出："RR.L"
解释：第一张多米诺骨牌没有给第二张施加额外的力。

输入：dominoes = ".L.R...LR..L.."
输出："LL.RR.LLRRLL.."
"""
"""
思路：找到字符串中的'.'，判断两端字符，如果两端字符相同，说明向一个方向倒，如果是左向右右向左的情况，则前一半向右右一半向左，
如果是左向左右向右的情况，则中间保持不动
"""


class Solution(object):
    @staticmethod
    def push_dominoes(dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        dominoes = 'L' + dominoes + 'R'
        n = len(dominoes)
        l = 0
        r = 1
        ans = []
        while r < n:
            while r < n and dominoes[r] == '.':
                r += 1
            left_char = dominoes[l]
            right_char = dominoes[r]
            if left_char == right_char:
                for i in range(l+1, r):
                    ans.append(left_char)
            elif left_char == 'R':
                for i in range((r-l-1) >> 1):
                    ans.append('R')
                if (r-l) & 1 == 0:
                    ans.append('.')
                for i in range((r-l-1) >> 1):
                    ans.append('L')
            else:
                for i in range(l+1, r):
                    ans.append('.')
            ans.append(right_char)
            l = r
            r += 1
        return ''.join(ans[:-1])

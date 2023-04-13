# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/4/12 10:23
"""
"""
你会得到一个字符串 text 。你应该把它分成 k 个子字符串 (subtext1, subtext2，…， subtextk) ，要求满足:
    subtexti 是 非空 字符串
    所有子字符串的连接等于 text ( 即subtext1 + subtext2 + ... + subtextk == text )
    对于所有 i 的有效值( 即 1 <= i <= k ) ，subtexti == subtextk - i + 1 均成立
返回k可能最大值。 

示例 1：
输入：text = "ghiabcdefhelloadamhelloabcdefghi"
输出：7
解释：我们可以把字符串拆分成 "(ghi)(abcdef)(hello)(adam)(hello)(abcdef)(ghi)"。

示例 2：
输入：text = "merchant"
输出：1
解释：我们可以把字符串拆分成 "(merchant)"。

示例 3：
输入：text = "antaprezatepzapreanta"
输出：11
解释：我们可以把字符串拆分成 "(a)(nt)(a)(pre)(za)(tpe)(za)(pre)(a)(nt)(a)"。
"""
"""
思路：双指针，从短到长枚举头部字符串和尾部字符串，看他们是否一样，一样的话就ans+2；同时用一个flag标记是否还能继续，如果结束了
flag还是False，那说明真结束了，ans+1。
"""


class Solution:
    @staticmethod
    def longestDecomposition(text: str) -> int:
        # n = len(text)
        # if n == 1:
        #     return 1
        # ans = 0
        # li, ri, lj, rj = 0, 1, n-1, n
        # while ri <= lj:
        #     while text[li:ri] != text[lj:rj]:
        #         ri += 1
        #         lj -= 1
        #     if li == lj and ri == rj:
        #         ans += 1
        #         break
        #     ans += 2
        #     li = ri
        #     ri += 1
        #     rj = lj
        #     lj -= 1
        #     if li == lj and ri == rj:
        #         ans += 1
        #         break
        # return ans

        ans = 0
        i, j = 0, len(text) - 1
        while i <= j:
            k = 1
            ok = False
            while i + k - 1 < j - k + 1:
                if text[i: i + k] == text[j - k + 1: j + 1]:
                    ans += 2
                    i += k
                    j -= k
                    ok = True
                    break
                k += 1
            if not ok:
                ans += 1
                break
        return ans

# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/3/29 10:59
"""
"""
给你一个整数 n，请返回长度为 n 、仅由元音 (a, e, i, o, u) 组成且按 字典序排列 的字符串数量。
字符串 s 按 字典序排列 需要满足：对于所有有效的 i，s[i] 在字母表中的位置总是与 s[i+1] 相同或在 s[i+1] 之前。 

示例 1：
输入：n = 1
输出：5
解释：仅由元音组成的 5 个字典序字符串为 ["a","e","i","o","u"]

示例 2：
输入：n = 2
输出：15
解释：仅由元音组成的 15 个字典序字符串为
["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"]
注意，"ea" 不是符合题意的字符串，因为 'e' 在字母表中的位置比 'a' 靠后

示例 3：
输入：n = 33
输出：66045
"""
"""
思路：
（1）dfs。一开始使用朴素dfs，超时。考虑记忆化搜索，将见过的状态记下来。
（2）dp。定义 f[i][j] 表示当前已经选了 i 个元音字母，且最后一个元音字母是 j 的方案数。初始时 f[1][j]=1。答案是 ∑j=0-4 f[n][j]。
我们可以发现 f[i][j] 只与 f[i−1][j] 有关，因此可以将二维数组压缩为一维数组，从而优化空间复杂度。
"""


class Solution:
    @staticmethod
    def countVowelStrings(n: int) -> int:
        # mapping = {
        #     'a': 0,
        #     'e': 1,
        #     'i': 2,
        #     'o': 3,
        #     'u': 4
        # }
        # ans = 0
        # def dfs(tmp, count):
        #     if count == n:
        #         nonlocal ans
        #         ans += 1
        #         return
        #     for letter in ['a', 'e', 'i', 'o', 'u']:
        #         if not tmp:
        #             dfs(tmp+letter, count+1)
        #         else:
        #             if mapping[letter] >= mapping[tmp[-1]]:
        #                 dfs(tmp+letter, count+1)
        # dfs('', 0)
        # return ans

        # @cache
        # def dfs(count, now):
        #     if count == n:
        #         return 1
        #     return sum(dfs(count + 1, k) for k in range(now, 5))
        # return dfs(0, 0)

        # @cache
        # def dfs(i, j):
        #     return 1 if i >= n else sum(dfs(i + 1, k) for k in range(j, 5))
        # return dfs(0, 0)

        f = [1] * 5
        for _ in range(n - 1):
            s = 0
            for j in range(5):
                s += f[j]
                f[j] = s
        return sum(f)

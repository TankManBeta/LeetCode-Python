# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/5/19 10:18
"""
from collections import Counter

"""
你有一套活字字模 tiles，其中每个字模上都刻有一个字母 tiles[i]。返回你可以印出的非空字母序列的数目。
注意：本题中，每个活字字模只能使用一次。 

示例 1：
输入："AAB"
输出：8
解释：可能的序列为 "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA"。

示例 2：
输入："AAABBC"
输出：188

示例 3：
输入："V"
输出：1
"""
"""
思路：
（1）回溯，每次从剩下的tiles中选择一个加入到字符集当中即可。
（2）计数+回溯，我们先用一个哈希表或数组 cnt 统计每个字母出现的次数。接下来定义一个函数 dfs(cnt)，表示当前剩余字母的计数为 cnt 
时，能够组成的不同序列的个数。在函数 dfs(cnt) 中，我们枚举 cnt 中每个大于 0 的值 cnt[i]，将 cnt[i] 减 1 表示使用了这个字母，
序列个数加 1，然后进行下一层搜索，在搜索结束后，累加返回的序列个数，然后将 cnt[i] 加 1（回溯，恢复现场）。最后返回序列个数。
"""


class Solution:
    @staticmethod
    def numTilePossibilities(tiles: str) -> int:
        # ans = set()
        # def helper(left,right):
        #     if left:
        #         ans.add(left)
        #     for i in range(len(right)):
        #         helper(left+right[i],right[:i]+right[i+1:])
        # helper('',tiles)
        # return len(ans)

        def dfs(cnt: Counter) -> int:
            ans = 0
            for i, x in cnt.items():
                if x > 0:
                    ans += 1
                    cnt[i] -= 1
                    ans += dfs(cnt)
                    cnt[i] += 1
            return ans

        cnt = Counter(tiles)
        return dfs(cnt)

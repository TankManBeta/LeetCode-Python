# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/3/26 14:30
"""
from linecache import cache

"""
给定正整数 n，返回在 [1, n] 范围内具有 至少 1 位 重复数字的正整数的个数。

示例 1：
输入：n = 20
输出：1
解释：具有至少 1 位重复数字的正数（<= 20）只有 11 。

示例 2：
输入：n = 100
输出：10
解释：具有至少 1 位重复数字的正数（<= 100）有 11，22，33，44，55，66，77，88，99 和 100 。

示例 3：
输入：n = 1000
输出：262
"""
"""
思路：题目要求统计 [1,..n] 中至少有一位重复的数字的个数，我们可以换一种思路，用一个函数 f(n) 统计 [1,..n] 中没有重复数字的个数，
那么答案就是 n−f(n)。
另外，我们可以用一个二进制数来记录数字中出现过的数字，比如数字中出现了 1, 2, 4，那么对应的二进制数就是 10110 。
接下来，我们用记忆化搜索来实现数位 DP。从起点向下搜索，到最底层得到方案数，一层层向上返回答案并累加，最后从搜索起点得到最终的答案。
基本步骤如下：
    将数字 n 转为整型数组 nums，其中 nums[0] 为最低位，而 nums[i] 为最高位；
    根据题目信息，设计函数 dfs()，对于本题，我们定义 dfs(pos,mask,lead,limit)，其中：
        参数 pos 表示当前搜索到的数字的位数，从末位或者第一位开始，一般根据题目的数字构造性质来选择顺序。对于本题，我们选择从高位
        开始，因此，pos 的初始值为数字的高位下标；
        参数 mask 表示当前数字中出现过的数字；
        参数 lead 表示当前数字是否仅包含前导零；
        参数 limit 表示当前可填的数字的限制，如果无限制，那么可以选择 i∈[0,1,..9]，否则，只能选择 i∈[0,..nums[pos]]。如果 limit 
        为 true 且已经取到了能取到的最大值，那么下一个 limit 同样为 true；如果 limit 为 true 但是还没有取到最大值，或者 limit 为 
        false，那么下一个 limit 为 false。
答案为 dfs(0,0,true,true)。
"""


class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        return n - self.f(n)

    @staticmethod
    def f(n: int) -> int:
        @cache
        def dfs(pos: int, mask: int, lead: bool, limit: bool) -> int:
            if pos < 0:
                return int(lead) ^ 1
            up = nums[pos] if limit else 9
            ans = 0
            for i in range(up + 1):
                if mask >> i & 1:
                    continue
                if i == 0 and lead:
                    ans += dfs(pos - 1, mask, lead, limit and i == up)
                else:
                    ans += dfs(pos - 1, mask | 1 << i, False, limit and i == up)
            return ans

        nums = []
        while n:
            nums.append(n % 10)
            n //= 10
        return dfs(len(nums) - 1, 0, True, True)

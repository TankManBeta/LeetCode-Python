# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/12/10 15:34
"""
from linecache import cache

"""
在 "100 game" 这个游戏中，两名玩家轮流选择从 1 到 10 的任意整数，累计整数和，先使得累计整数和 达到或超过  100 的玩家，即为胜者。
如果我们将游戏规则改为 “玩家 不能 重复使用整数” 呢？
例如，两个玩家可以轮流从公共整数池中抽取从 1 到 15 的整数（不放回），直到累计整数和 >= 100。
给定两个整数 maxChoosableInteger （整数池中可选择的最大数）和 desiredTotal（累计和），若先出手的玩家是否能稳赢则返回 true ，
否则返回 false 。假设两位玩家游戏时都表现 最佳 。

示例 1：
输入：maxChoosableInteger = 10, desiredTotal = 11
输出：false
解释：
无论第一个玩家选择哪个整数，他都会失败。
第一个玩家可以选择从 1 到 10 的整数。
如果第一个玩家选择 1，那么第二个玩家只能选择从 2 到 10 的整数。
第二个玩家可以通过选择整数 10（那么累积和为 11 >= desiredTotal），从而取得胜利.
同样地，第一个玩家选择任意其他整数，第二个玩家都会赢。

示例 2:
输入：maxChoosableInteger = 10, desiredTotal = 0
输出：true

示例 3:
输入：maxChoosableInteger = 10, desiredTotal = 1
输出：true
"""
"""
思路：在游戏中途，假设已经被使用的数字的集合为 usedNumbers，这些数字的和为 currentTotal。当某方行动时，如果他能在未选择的数字
中选出一个 i，使得 i+currentTotal≥desiredTotal，则他能获胜。否则，需要继续通过搜索来判断获胜方。在剩下的数字中，
如果他能选择一个 i，使得对方在接下来的局面中无法获胜，则他会获胜。否则，他会失败。
"""


class Solution:
    @staticmethod
    def canIWin(maxChoosableInteger: int, desiredTotal: int) -> bool:
        @cache
        def dfs(usedNumbers: int, currentTotal: int) -> bool:
            for i in range(maxChoosableInteger):
                if (usedNumbers >> i) & 1 == 0:
                    if currentTotal + i + 1 >= desiredTotal or not dfs(usedNumbers | (1 << i), currentTotal + i + 1):
                        return True
            return False

        return (1 + maxChoosableInteger) * maxChoosableInteger // 2 >= desiredTotal and dfs(0, 0)

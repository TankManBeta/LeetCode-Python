# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/1/28 13:32
"""
"""
你正在参加一个多角色游戏，每个角色都有两个主要属性：攻击和防御 。给你一个二维整数数组 properties，
其中 properties[i] = [attacki, defensei] 表示游戏中第 i 个角色的属性。
如果存在一个其他角色的攻击和防御等级 都严格高于 该角色的攻击和防御等级，则认为该角色为弱角色。
更正式地，如果认为角色 i 弱于 存在的另一个角色 j ，那么 attack[j] > attack[i] 且 defense[j] > defense[i] 。
返回 弱角色 的数量。

输入：properties = [[5,5],[6,3],[3,6]]
输出：0
解释：不存在攻击和防御都严格高于其他角色的角色。

输入：properties = [[2,2],[3,3]]
输出：1
解释：第一个角色是弱角色，因为第二个角色的攻击和防御严格大于该角色。

输入：properties = [[1,5],[10,4],[4,3]]
输出：1
解释：第三个角色是弱角色，因为第二个角色的攻击和防御严格大于该角色。
"""
"""
思路：按照攻击降序，且攻击相同时防御升序排列，记录最大防御，假设当前的防御比之前的最大防御小，即可确认当前的是弱角色，
理由是：在相同的攻击内，防御是升序，出现的防御大于当前，肯定是来自于攻击更大的那些组。
"""


class Solution(object):
    @staticmethod
    def number_of_weak_characters(properties):
        """
        :type properties: List[List[int]]
        :rtype: int
        """
        properties.sort(key=lambda x: (-x[0], x[1]))
        ans = 0
        max_defense = 0
        for _, defense in properties:
            if max_defense > defense:
                ans += 1
            else:
                max_defense = max(max_defense, defense)
        return ans

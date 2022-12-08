# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/12/7 11:55
"""
from typing import List

"""
给你一个数组 items ，其中 items[i] = [typei, colori, namei] ，描述第 i 件物品的类型、颜色以及名称。
另给你一条由两个字符串 ruleKey 和 ruleValue 表示的检索规则。
如果第 i 件物品能满足下述条件之一，则认为该物品与给定的检索规则 匹配 ：
ruleKey == "type" 且 ruleValue == typei 。
ruleKey == "color" 且 ruleValue == colori 。
ruleKey == "name" 且 ruleValue == namei 。
统计并返回 匹配检索规则的物品数量 。

示例 1：
输入：items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], ruleKey = "color", ruleValue = "silver"
输出：1
解释：只有一件物品匹配检索规则，这件物品是 ["computer","silver","lenovo"] 。

示例 2：
输入：items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]], ruleKey = "type", ruleValue = "phone"
输出：2
解释：只有两件物品匹配检索规则，这两件物品分别是 ["phone","blue","pixel"] 和 ["phone","gold","iphone"]。注意，["computer","silver","phone"] 未匹配检索规则。
"""
"""
思路：直接按要求模拟即可
"""


class Solution:
    @staticmethod
    def countMatches(items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        mapping = {
            "type": 0,
            "color": 1,
            "name": 2
        }
        index = mapping[ruleKey]
        ans = 0
        for item in items:
            if item[index] == ruleValue:
                ans += 1
        return ans

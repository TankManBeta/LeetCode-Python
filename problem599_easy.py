# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/3/14 9:41
"""
"""
假设 Andy 和 Doris 想在晚餐时选择一家餐厅，并且他们都有一个表示最喜爱餐厅的列表，每个餐厅的名字用字符串表示。
你需要帮助他们用最少的索引和找出他们共同喜爱的餐厅。 如果答案不止一个，则输出所有答案并且不考虑顺序。 你可以假设答案总是存在。

输入: list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]，list2 = ["Piatti", "The Grill at Torrey Pines", 
"Hungry Hunter Steakhouse", "Shogun"]
输出: ["Shogun"]
解释: 他们唯一共同喜爱的餐厅是“Shogun”。

输入:list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]，list2 = ["KFC", "Shogun", "Burger King"]
输出: ["Shogun"]
解释: 他们共同喜爱且具有最小索引和的餐厅是“Shogun”，它有最小的索引和1(0+1)。
"""
"""
思路：直接模拟即可，索引和比当前最小索引和小就先清空再添加，相等就直接添加，大于就继续下一个
"""


class Solution(object):
    @staticmethod
    def find_restaurant(list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        n = len(list1)
        m = len(list2)
        index_sum = n+m
        res = []
        for i in range(n):
            if list1[i] in list2:
                index = list2.index(list1[i])
            else:
                continue
            if index + i < index_sum:
                res = [list1[i]]
                index_sum = index+i
            elif index + i == index_sum:
                res.append(list1[i])
        return res

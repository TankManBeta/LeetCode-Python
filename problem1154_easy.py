# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2021/12/21 13:28
"""
"""
给你一个字符串 date ，按 YYYY-MM-DD 格式表示一个 现行公元纪年法 日期。请你计算并返回该日期是当年的第几天。
通常情况下，我们认为1月1日是每年的第1天，1月2日是每年的第2天，依此类推。每个月的天数与现行公元纪年法（格里高利历）一致。

输入：date = "2019-01-09"
输出：9

输入：date = "2019-02-10"
输出：41

输入：date = "2003-03-01"
输出：60

输入：date = "2004-03-01"
输出：61
"""
"""
思路：判断是否为闰年，然后累加就行
"""


class Solution(object):
    @staticmethod
    def day_of_year(date):
        """
        :type date: str
        :rtype: int
        """
        date_str = date.split('-')
        date_list = [int(value) for value in date_str]
        if date_list[0] % 400 == 0:
            is_leap = 1
        else:
            if date_list[0] % 4 == 0 and date_list[0] % 100 != 0:
                is_leap = 1
            else:
                is_leap = 0
        if is_leap == 1:
            days_of_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        else:
            days_of_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        total_days = 0
        for i in range(0, date_list[1]-1):
            total_days += days_of_month[i]
        total_days += date_list[2]
        return total_days

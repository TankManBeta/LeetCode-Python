# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/5/17 9:54
"""
from typing import List

"""
给你两个字符串数组 event1 和 event2 ，表示发生在同一天的两个闭区间时间段事件，其中：
    event1 = [startTime1, endTime1] 且
    event2 = [startTime2, endTime2]
事件的时间为有效的 24 小时制且按 HH:MM 格式给出。
当两个事件存在某个非空的交集时（即，某些时刻是两个事件都包含的），则认为出现 冲突 。
如果两个事件之间存在冲突，返回 true ；否则，返回 false 。 

示例 1：
输入：event1 = ["01:15","02:00"], event2 = ["02:00","03:00"]
输出：true
解释：两个事件在 2:00 出现交集。

示例 2：
输入：event1 = ["01:00","02:00"], event2 = ["01:20","03:00"]
输出：true
解释：两个事件的交集从 01:20 开始，到 02:00 结束。

示例 3：
输入：event1 = ["10:00","11:00"], event2 = ["14:00","15:00"]
输出：false
解释：两个事件不存在交集。
"""
"""
思路：
（1）把字符串转成秒，然后再判断
（2）也可以不用转换，直接比较字符串即可
"""


class Solution:
    @staticmethod
    def haveConflict(event1: List[str], event2: List[str]) -> bool:
        # hour1, minute1 = map(int, event1[0].split(':'))
        # hour2, minute2 = map(int, event1[1].split(':'))
        # hour3, minute3 = map(int, event2[0].split(':'))
        # hour4, minute4 = map(int, event2[1].split(':'))
        # second1 = hour1 * 60 + minute1
        # second2 = hour2 * 60 + minute2
        # second3 = hour3 * 60 + minute3
        # second4 = hour4 * 60 + minute4
        # if second4 < second1 or second3 > second2:
        #     return False
        # else:
        #     return True

        return not (event1[0] > event2[1] or event1[1] < event2[0])

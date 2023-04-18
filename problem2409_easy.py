# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/4/17 10:21
"""
"""
Alice 和 Bob 计划分别去罗马开会。
给你四个字符串 arriveAlice ，leaveAlice ，arriveBob 和 leaveBob 。Alice 会在日期 arriveAlice 到 leaveAlice 之间在城市里
（日期为闭区间），而 Bob 在日期 arriveBob 到 leaveBob 之间在城市里（日期为闭区间）。每个字符串都包含 5 个字符，格式为 "MM-DD"，
对应着一个日期的月和日。
请你返回 Alice和 Bob 同时在罗马的天数。
你可以假设所有日期都在 同一个 自然年，而且 不是 闰年。每个月份的天数分别为：[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 。 

示例 1：
输入：arriveAlice = "08-15", leaveAlice = "08-18", arriveBob = "08-16", leaveBob = "08-19"
输出：3
解释：Alice 从 8 月 15 号到 8 月 18 号在罗马。Bob 从 8 月 16 号到 8 月 19 号在罗马，他们同时在罗马的日期为 8 月 16、17 和 18 号。所以答案为 3 。

示例 2：
输入：arriveAlice = "10-01", leaveAlice = "10-31", arriveBob = "11-01", leaveBob = "12-31"
输出：0
解释：Alice 和 Bob 没有同时在罗马的日子，所以我们返回 0 。
"""
"""
思路：算出是一年中的第几天，然后算有多少区间是重叠的即可。
"""


class Solution:
    @staticmethod
    def countDaysTogether(arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        # days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        # def convert_date(arrive, leave):
        #     arrive_month, arrive_day = map(int, arrive.split('-'))
        #     leave_month, leave_day = map(int, leave.split('-'))
        #     full_arrive = sum([days[i] for i in range(arrive_month-1)])
        #     start = full_arrive + arrive_day
        #     full_leave = sum([days[i] for i in range(leave_month-1)])
        #     end = full_leave + leave_day
        #     return start, end

        # start1, end1 = convert_date(arriveAlice, leaveAlice)
        # start2, end2 = convert_date(arriveBob, leaveBob)

        # if end2 < start1 or start2 > end1:
        #     return 0
        # if start1 <= start2 <= end1 and start1 <= end2 <= end1:
        #     return end2 - start2 + 1
        # if start2 <= start1 and end2 >= end1:
        #     return end1 - start1 + 1
        # if start2 < start1 and start1 <= end2 <= end1:
        #     return end2 - start1 + 1
        # if end2 > end1 and start1 <= start2 <= end1:
        #     return end1 - start2 + 1

        a = max(arriveAlice, arriveBob)
        b = min(leaveAlice, leaveBob)
        days = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
        x = sum(days[:int(a[:2]) - 1]) + int(a[3:])
        y = sum(days[:int(b[:2]) - 1]) + int(b[3:])
        return max(y - x + 1, 0)

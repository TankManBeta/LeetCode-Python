# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/1/18 12:19
"""
"""
给定一个 24 小时制（小时:分钟 "HH:MM"）的时间列表，找出列表中任意两个时间的最小时间差并以分钟数表示。

输入：timePoints = ["23:59","00:00"]
输出：1

输入：timePoints = ["00:00","23:59","00:00"]
输出：0
"""
"""
思路：最短时间间隔必定出现在相邻或头尾之间，所以直接先排序，然后计算即可。（看完题解之后发现可以用鸽巢原理改进一下，太妙了）
"""


class Solution(object):
    @staticmethod
    def find_min_difference(time_points):
        """
        :type time_points: List[str]
        :rtype: int
        """
        sorted_time = sorted(time_points)
        len_time = len(time_points)
        min_interval = 1440
        for i in range(0, len_time-1):
            temp1 = sorted_time[i].split(":")
            temp1_hour = int(temp1[0])
            temp1_minute = int(temp1[1])
            temp2 = sorted_time[i+1].split(":")
            temp2_hour = int(temp2[0])
            temp2_minute = int(temp2[1])
            temp_minutes = (temp2_hour - temp1_hour)*60 + temp2_minute - temp1_minute
            if temp_minutes < min_interval:
                min_interval = temp_minutes
        last = sorted_time[-1].split(":")
        first = sorted_time[0].split(":")
        last_hour = int(last[0])
        last_minute = int(last[1])
        first_hour = int(first[0])
        first_minute = int(first[1])
        last_first_interval = (23-last_hour)*60 + 60 - last_minute + first_hour*60 + first_minute
        if last_first_interval < min_interval:
            min_interval = last_first_interval
        return min_interval

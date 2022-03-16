# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/3/15 10:33
"""
"""
给你一个数组 points ，其中 points[i] = [xi, yi] 表示 X-Y 平面上的一个点。求最多有多少个点在同一条直线上。

输入：points = [[1,1],[2,2],[3,3]]
输出：3

输入：points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
输出：4
"""
"""
思路：对每一个点计算与其他点的斜率，然后count即可
"""


class Solution(object):
    @staticmethod
    def max_points(points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        count_list = [0]*n
        for i in range(n):
            count_dict = {"me": 0}
            for j in range(n):
                if i == j:
                    continue
                else:
                    if points[j][0] == points[i][0]:
                        count_dict[2*10**4+1] = count_dict.get(2*10**4+1, 0)+1
                    else:
                        k = float(points[j][1]-points[i][1])/(points[j][0]-points[i][0])
                        count_dict[k] = count_dict.get(k, 0)+1
            count_list[i] = max(count_dict.values())+1
        return max(count_list)

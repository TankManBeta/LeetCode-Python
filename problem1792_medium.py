# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/2/19 14:26
"""
from heapq import heapify, heappop, heappush
from typing import List

"""
一所学校里有一些班级，每个班级里有一些学生，现在每个班都会进行一场期末考试。给你一个二维数组 classes ，其中 classes[i] = 
[passi, totali] ，表示你提前知道了第 i 个班级总共有 totali 个学生，其中只有 passi 个学生可以通过考试。
给你一个整数 extraStudents ，表示额外有 extraStudents 个聪明的学生，他们 一定 能通过任何班级的期末考。你需要给这 
extraStudents 个学生每人都安排一个班级，使得 所有 班级的 平均 通过率 最大 。
一个班级的 通过率 等于这个班级通过考试的学生人数除以这个班级的总人数。平均通过率 是所有班级的通过率之和除以班级数目。
请你返回在安排这 extraStudents 个学生去对应班级后的 最大 平均通过率。与标准答案误差范围在 10-5 以内的结果都会视为正确结果。

示例 1：
输入：classes = [[1,2],[3,5],[2,2]], extraStudents = 2
输出：0.78333
解释：你可以将额外的两个学生都安排到第一个班级，平均通过率为 (3/4 + 3/5 + 2/2) / 3 = 0.78333 。

示例 2：
输入：classes = [[2,4],[3,9],[4,5],[2,10]], extraStudents = 4
输出：0.53485
"""
"""
思路：因为班级数量是不变的，所以我们只需要保证每一次加入班级之后，通过率变化量最大，所以我们针对通过率变化量制造一个优先队列
（增量大根堆）。进行 extraStudents 次操作，每次从堆顶取出一个班级，将这个班级的人数和通过人数都加 1，然后将这个班级的通过率增量
重新计算并放回堆中。重复这个过程，直到将所有的学生都分配完毕。最后，我们将所有班级的通过率求和，然后除以班级数目，即为答案。
"""


class Solution:
    @staticmethod
    def maxAverageRatio(classes: List[List[int]], extraStudents: int) -> float:
        h = [(a / b - (a + 1) / (b + 1), a, b) for a, b in classes]
        heapify(h)
        for _ in range(extraStudents):
            _, a, b = heappop(h)
            a, b = a + 1, b + 1
            heappush(h, (a / b - (a + 1) / (b + 1), a, b))
        return sum(v[1] / v[2] for v in h) / len(classes)

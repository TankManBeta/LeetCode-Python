# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/2/11 13:18
"""
"""
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
求在该柱状图中，能够勾勒出来的矩形的最大面积。

输入：heights = [2,1,5,6,2,3]
输出：10
解释：最大的矩形为图中红色区域，面积为 10

输入： heights = [2,4]
输出： 4
"""
"""
思路：单调栈
单调栈分为单调递增栈和单调递减栈
11. 单调递增栈即栈内元素保持单调递增的栈
12. 同理单调递减栈即栈内元素保持单调递减的栈
操作规则（下面都以单调递增栈为例）
21. 如果新的元素比栈顶元素大，就入栈
22. 如果新的元素较小，那就一直把栈内元素弹出来，直到栈顶比新元素小
加入这样一个规则之后，会有什么效果
31. 栈内的元素是递增的
32. 当元素出栈时，说明这个新元素是出栈元素向后找第一个比其小的元素
举个例子，配合下图，现在索引在 6 ，栈里是 1 5 6 。
接下来新元素是 2 ，那么 6 需要出栈。
当 6 出栈时，右边 2 代表是 6 右边第一个比 6 小的元素。
当元素出栈后，说明新栈顶元素是出栈元素向前找第一个比其小的元素
当 6 出栈时，5 成为新的栈顶，那么 5 就是 6 左边第一个比 6 小的元素。

对于一个高度，如果能得到向左和向右的边界
那么就能对每个高度求一次面积
遍历所有高度，即可得出最大面积
使用单调栈，在出栈操作时得到前后边界并计算面积
注意增加哨兵，解决弹栈的时候，栈为空和遍历完成以后，栈中还有元素的情况
"""


class Solution(object):
    @staticmethod
    def largest_rectangle_area(heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights = [0] + heights + [0]
        m = len(heights)
        res = 0
        stack = []
        for i in range(m):
            # 如果当前要进栈的元素比栈顶元素小，说明当前要进栈的元素是栈顶元素右边第一个最小的，同时弹出栈顶元素后的新栈顶元素是
            # 原栈顶元素左边第一个最小的元素
            while stack and heights[stack[-1]] > heights[i]:
                temp = stack.pop()
                res = max(res, (i - stack[-1] - 1) * heights[temp])
            stack.append(i)
        return res
# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/3/8 10:17
"""
"""
n 个孩子站成一排。给你一个整数数组 ratings 表示每个孩子的评分。
你需要按照以下要求，给这些孩子分发糖果：
    每个孩子至少分配到 1 个糖果。
    相邻两个孩子评分更高的孩子会获得更多的糖果。
请你给每个孩子分发糖果，计算并返回需要准备的 最少糖果数目 。

输入：ratings = [1,0,2]
输出：5
解释：你可以分别给第一个、第二个、第三个孩子分发 2、1、2 颗糖果。

输入：ratings = [1,2,2]
输出：4
解释：你可以分别给第一个、第二个、第三个孩子分发 1、2、1 颗糖果。
     第三个孩子只得到 1 颗糖果，这满足题面中的两个条件。
"""
"""
思路：
（1）从左往右的规则是后面一个比前面一个大就加1，否则变为1；从右往左的规则是前面一个比后面一个大就加1，否则变为1；然后取两个里
面大的一个加起来即可。
（2）一次遍历，记前一个同学分配的糖果数为pre，当前同学评分>=前一个同学评分，等的话分配1个，否则pre+1个，increase=pre，升序序列
的长度就等于pre的长度；如果小的话，decrease++，因为只需要分配一个，如果持续小的话，则前面需要比后面大一个（便于自己理解），如果
递增和递减长度相同需要把递增的最后一个送给递减
"""


class Solution(object):
    @staticmethod
    def candy(ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        # n = len(ratings)
        # res = 0
        # left = [0]*n
        # right = [0]*n
        # left[0] = 1
        # right[n-1] = 1
        # for i in range(1, n):
        #     if ratings[i] > ratings[i-1]:
        #         left[i] = left[i-1] + 1
        #     else:
        #         left[i] = 1
        # for i in range(n-2, -1, -1):
        #     if ratings[i] > ratings[i+1]:
        #         right[i] = right[i+1] + 1
        #     else:
        #         right[i] = 1
        # for i in range(n):
        #     res += max(left[i], right[i])
        # return res

        n = len(ratings)
        res = 1
        pre = 1
        increase = 1
        decrease = 0
        for i in range(1, n):
            if ratings[i] >= ratings[i-1]:
                decrease = 0
                pre = (1 if ratings[i] == ratings[i-1] else pre+1)
                res += pre
                increase = pre
            else:
                decrease += 1
                if decrease == increase:
                    decrease += 1
                res += decrease
                pre = 1
        return res

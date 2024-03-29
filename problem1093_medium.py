# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/5/27 16:51
"""
from typing import List

"""
我们对 0 到 255 之间的整数进行采样，并将结果存储在数组 count 中：count[k] 就是整数 k 在样本中出现的次数。
计算以下统计数据:
    minimum ：样本中的最小元素。
    maximum ：样品中的最大元素。
    mean ：样本的平均值，计算为所有元素的总和除以元素总数。
    median ：
        如果样本的元素个数是奇数，那么一旦样本排序后，中位数 median 就是中间的元素。
        如果样本中有偶数个元素，那么中位数median 就是样本排序后中间两个元素的平均值。
    mode ：样本中出现次数最多的数字。保众数是 唯一 的。
以浮点数数组的形式返回样本的统计信息 [minimum, maximum, mean, median, mode] 。与真实答案误差在 10-5 内的答案都可以通过。

示例 1：
输入：count = [0,1,3,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
输出：[1.00000,3.00000,2.37500,2.50000,3.00000]
解释：用count表示的样本为[1,2,2,2,3,3,3,3]。
最小值和最大值分别为1和3。
均值是(1+2+2+2+3+3+3+3) / 8 = 19 / 8 = 2.375。
因为样本的大小是偶数，所以中位数是中间两个元素2和3的平均值，也就是2.5。
众数为3，因为它在样本中出现的次数最多。

示例 2：
输入：count = [0,4,3,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
输出：[1.00000,4.00000,2.18182,2.00000,1.00000]
解释：用count表示的样本为[1,1,1,1,2,2,3,3,3,4,4]。
最小值为1，最大值为4。
平均数是(1+1+1+1+2+2+2+3+3+4+4)/ 11 = 24 / 11 = 2.18181818…(为了显示，输出显示了整数2.18182)。
因为样本的大小是奇数，所以中值是中间元素2。
众数为1，因为它在样本中出现的次数最多。
"""
"""
思路：直接模拟即可
"""


class Solution:
    @staticmethod
    def sampleStats(count: List[int]) -> List[float]:
        n = len(count)
        total = 0
        cnt = 0
        max_cnt = 0
        max_cnt_num = -1
        maximum = -1
        minimum = 256
        for j in range(n - 1, -1, -1):
            if count[j] != 0:
                maximum = max(maximum, j)
                total += j * count[j]
                cnt += count[j]
                if count[j] > max_cnt:
                    max_cnt = count[j]
                    max_cnt_num = j
        if cnt % 2 == 0:
            left, right = cnt // 2, cnt // 2 + 1
            left_val, right_val = 0, 0
            tmp_cnt = 0
            for i in range(n):
                if count[i] != 0:
                    minimum = min(i, minimum)
                    tmp_cnt += count[i]
                    if tmp_cnt >= left > tmp_cnt - count[i]:
                        left_val = i
                    if tmp_cnt >= right > tmp_cnt - count[i]:
                        right_val = i
            median = (left_val + right_val) / 2
        else:
            mid = cnt // 2 + 1
            mid_val = 0
            tmp_cnt = 0
            for i in range(n):
                if count[i] != 0:
                    minimum = min(i, minimum)
                    tmp_cnt += count[i]
                    if tmp_cnt >= mid > tmp_cnt - count[i]:
                        mid_val = i
            median = mid_val
        return [minimum, maximum, total / cnt, median, max_cnt_num]

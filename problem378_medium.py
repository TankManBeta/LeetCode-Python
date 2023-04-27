# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/4/26 10:37
"""
from typing import List

"""
给你一个 n x n 矩阵 matrix ，其中每行和每列元素均按升序排序，找到矩阵中第 k 小的元素。
请注意，它是 排序后 的第 k 小元素，而不是第 k 个 不同 的元素。
你必须找到一个内存复杂度优于 O(n2) 的解决方案。 

示例 1：
输入：matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
输出：13
解释：矩阵中的元素为 [1,5,9,10,11,12,13,13,15]，第 8 小元素是 13

示例 2：
输入：matrix = [[-5]], k = 1
输出：-5
"""
"""
思路：二分，矩阵中左上角的数一定是最小的，记为low，右下角的一定是最大的high，中间的(low+high)//2记为mid，然后统计比mid小的有
多少个，如果小于k，说明数字不够多，low=mid+1；否则说明数字太多了，high=mid，最后返回最左边的数即可。
"""


class Solution:
    @staticmethod
    def kthSmallest(matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        def get_count(num):
            cnt = 0
            i, j = 0, n - 1
            while i < n and j >= 0:
                if matrix[i][j] <= num:
                    cnt += j + 1
                    i += 1
                else:
                    j -= 1
            return cnt

        low, high = matrix[0][0], matrix[n - 1][n - 1]
        while low < high:
            mid = (low + high) // 2
            if get_count(mid) < k:
                low = mid + 1
            else:
                high = mid
        return low

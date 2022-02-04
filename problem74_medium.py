# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/2/3 12:35
"""
"""
编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：
每行中的整数从左到右按升序排列。
每行的第一个整数大于前一行的最后一个整数。

输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
输出：true

输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
输出：false
"""
"""
思路：
（1）两次二分，第一次找在的行，第二次找在的列
（2）左下角开始搜索，如果比当前小就往上找，如果比当前大就往右找
"""


class Solution(object):
    @staticmethod
    def search_matrix(matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0])
        up = 0
        down = m - 1
        left = 0
        right = n - 1
        mid = -1
        while up <= down:
            mid = (up + down) / 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                break
            elif target < matrix[mid][0]:
                down = mid - 1
            else:
                up = mid + 1
        a = mid
        while left <= right:
            mid = (left + right) / 2
            if matrix[a][mid] == target:
                return True
            elif target < matrix[a][mid]:
                right = mid - 1
            else:
                left = mid + 1
        return False

        # m = len(matrix)
        # n = len(matrix[0])
        # row = m-1
        # col = 0
        # while True:
        #     if row<0 or col>n-1:
        #         return False
        #     if matrix[row][col] == target:
        #         return True
        #     elif matrix[row][col] < target:
        #         col += 1
        #     else:
        #         row -= 1

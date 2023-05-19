# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/5/18 10:12
"""
from typing import List

"""
给出基数为 -2 的两个数 arr1 和 arr2，返回两数相加的结果。
数字以 数组形式 给出：数组由若干 0 和 1 组成，按最高有效位到最低有效位的顺序排列。例如，arr = [1,1,0,1] 表示数字 (-2)^3 + 
(-2)^2 + (-2)^0 = -3。数组形式 中的数字 arr 也同样不含前导零：即 arr == [0] 或 arr[0] == 1。
返回相同表示形式的 arr1 和 arr2 相加的结果。两数的表示形式为：不含前导零、由若干 0 和 1 组成的数组。

示例 1：
输入：arr1 = [1,1,1,1,1], arr2 = [1,0,1]
输出：[1,0,0,0,0]
解释：arr1 表示 11，arr2 表示 5，输出表示 16 。

示例 2：
输入：arr1 = [0], arr2 = [0]
输出：[0]

示例 3：
输入：arr1 = [0], arr2 = [1]
输出：[1]
"""
"""
思路：我们遍历两个数组，从最低位开始，记两个数组当前位的数字为 a 和 b，进位为 c，三个数相加的结果为 x。
先将进位 c 置为 0。
    如果 x≥2，那么将 x 减去 2，并向高位进位 −1。即逢 2 进负 1。
    如果 x=−1，由于 −(−2)^i=(−2)^i+(−2)^(i+1)，所以我们可以将 x 置为 1，并向高位进位 1。
然后，我们将 x 加入到答案数组中，然后继续处理下一位。
遍历结束后，去除答案数组中末尾的 0，并将数组反转，即可得到最终的答案。
"""


class Solution:
    @staticmethod
    def addNegabinary(arr1: List[int], arr2: List[int]) -> List[int]:
        i, j = len(arr1) - 1, len(arr2) - 1
        c = 0
        ans = []
        while i >= 0 or j >= 0 or c:
            a = 0 if i < 0 else arr1[i]
            b = 0 if j < 0 else arr2[j]
            x = a + b + c
            c = 0
            if x >= 2:
                x -= 2
                c -= 1
            elif x == -1:
                x = 1
                c += 1
            ans.append(x)
            i, j = i - 1, j - 1
        while len(ans) > 1 and ans[-1] == 0:
            ans.pop()
        return ans[::-1]

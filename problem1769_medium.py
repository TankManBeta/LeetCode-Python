# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/12/2 11:04
"""
from typing import List

"""
有 n 个盒子。给你一个长度为 n 的二进制字符串 boxes ，其中 boxes[i] 的值为 '0' 表示第 i 个盒子是 空 的，
而 boxes[i] 的值为 '1' 表示盒子里有 一个 小球。
在一步操作中，你可以将 一个 小球从某个盒子移动到一个与之相邻的盒子中。第 i 个盒子和第 j 个盒子相邻需满足 abs(i - j) == 1 。
注意，操作执行后，某些盒子中可能会存在不止一个小球。
返回一个长度为 n 的数组 answer ，其中 answer[i] 是将所有小球移动到第 i 个盒子所需的 最小 操作数。
每个 answer[i] 都需要根据盒子的 初始状态 进行计算。

示例 1：
输入：boxes = "110"
输出：[1,1,3]
解释：每个盒子对应的最小操作数如下：
1) 第 1 个盒子：将一个小球从第 2 个盒子移动到第 1 个盒子，需要 1 步操作。
2) 第 2 个盒子：将一个小球从第 1 个盒子移动到第 2 个盒子，需要 1 步操作。
3) 第 3 个盒子：将一个小球从第 1 个盒子移动到第 3 个盒子，需要 2 步操作。将一个小球从第 2 个盒子移动到第 3 个盒子，需要 1 步操作。共计 3 步操作。

示例 2：
输入：boxes = "001011"
输出：[11,8,5,4,3,4]
"""
"""
思路：要求将所有球移动到i的最小次数，也就是把i左边的球和右边的球移动到i的次数之和。以将i左边的球都移动到i为例，又可以分解为
移动到i-1所需要的最小步数+全部移动到i-1之后i-1中拥有的小球的数量（前缀和）。
"""


class Solution:
    @staticmethod
    def minOperations(boxes: str) -> List[int]:
        n = len(boxes)
        res_left = [0] * n
        res_right = [0] * n
        left = 0
        right = 0
        for i in range(n):
            res_left[i] = res_left[i - 1] + left
            if boxes[i] == '1':
                left += 1
        for j in range(n - 1, -1, -1):
            res_right[j] = res_right[(j + 1) % n] + right
            if boxes[j] == '1':
                right += 1
        return [res_left[i] + res_right[i] for i in range(n)]

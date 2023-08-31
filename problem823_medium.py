# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/8/30 22:16
"""
from typing import List

"""
给出一个含有不重复整数元素的数组 arr ，每个整数 arr[i] 均大于 1。
用这些整数来构建二叉树，每个整数可以使用任意次数。其中：每个非叶结点的值应等于它的两个子结点的值的乘积。
满足条件的二叉树一共有多少个？答案可能很大，返回 对 109 + 7 取余 的结果。 

示例 1:
输入: arr = [2, 4]
输出: 3
解释: 可以得到这些二叉树: [2], [4], [4, 2, 2]

示例 2:
输入: arr = [2, 4, 5, 10]
输出: 7
解释: 可以得到这些二叉树: [2], [4], [5], [10], [4, 2, 2], [10, 2, 5], [10, 5, 2].
"""
"""
思路：我们可以枚举 arr 中的每一个数 a 作为二叉树的根节点（根节点一定最大），然后枚举枚举左子树的值 b，若 a 能被 b 整除，则右子树的值为 a/b，
若 a/b 也在 arr 中，则可以构成一棵二叉树。此时，以 a 为根节点的二叉树的个数为 f(a)=f(b)×f(a/b)，其中 f(b) 和 f(a/b) 分别为左子树和
右子树的二叉树个数。因此，我们先将 arr 排序，然后用 f[i] 表示以 arr[i] 为根节点的二叉树的个数，最终答案即为 f[0]+f[1]+⋯+f[n−1]。注意
答案可能很大，需要对 10**9+7 取模。
"""


class Solution:
    @staticmethod
    def numFactoredBinaryTrees(arr: List[int]) -> int:
        mod = 10**9 + 7
        n = len(arr)
        arr.sort()
        idx = {v: i for i, v in enumerate(arr)}
        f = [1] * n
        for i, a in enumerate(arr):
            for j in range(i):
                b = arr[j]
                if a % b == 0 and (a // b) in idx:
                    f[i] = (f[i] + f[j] * f[idx[a // b]]) % mod
        return sum(f) % mod

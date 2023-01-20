# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/1/19 20:17
"""
from typing import List

"""
给定一个整数数组 asteroids，表示在同一行的行星。
对于数组中的每一个元素，其绝对值表示行星的大小，正负表示行星的移动方向（正表示向右移动，负表示向左移动）。每一颗行星以相同的速度移动。
找出碰撞后剩下的所有行星。
碰撞规则：两个行星相互碰撞，较小的行星会爆炸。如果两颗行星大小相同，则两颗行星都会爆炸。两颗移动方向相同的行星，永远不会发生碰撞。

示例 1：
输入：asteroids = [5,10,-5]
输出：[5,10]
解释：10 和 -5 碰撞后只剩下 10 。 5 和 10 永远不会发生碰撞。

示例 2：
输入：asteroids = [8,-8]
输出：[]
解释：8 和 -8 碰撞后，两者都发生爆炸。

示例 3：
输入：asteroids = [10,2,-5]
输出：[10]
解释：2 和 -5 发生碰撞后剩下 -5 。10 和 -5 发生碰撞后剩下 10 。
"""
"""
思路：使用栈 st （向右为正方向）模拟行星碰撞，从左往右遍历行星数组 asteroids，当我们遍历到行星 aster 时，使用变量 alive 记录
行星 aster 是否还存在（即未爆炸）。当行星 aster 存在且 aster<0，栈顶元素非空且大于 0 时，说明两个行星相互向对方移动：如果栈顶
元素大于等于 −aster，则行星 aster 发生爆炸，将 alive 置为 false；如果栈顶元素小于等于 −aster，则栈顶元素表示的行星发生爆炸，
执行出栈操作。重复以上判断直到不满足条件，如果最后 alive 为真，说明行星 aster 不会爆炸，则将 aster 入栈。
"""


class Solution:
    @staticmethod
    def asteroidCollision(asteroids: List[int]) -> List[int]:
        st = []
        for aster in asteroids:
            alive = True
            while alive and aster < 0 and st and st[-1] > 0:
                alive = st[-1] < -aster
                if st[-1] <= -aster:
                    st.pop()
            if alive:
                st.append(aster)
        return st

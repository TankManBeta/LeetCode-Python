# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/8/21 19:38
"""
"""
给你两个字符串 start 和 target ，长度均为 n 。每个字符串 仅 由字符 'L'、'R' 和 '_' 组成，其中：
字符 'L' 和 'R' 表示片段，其中片段 'L' 只有在其左侧直接存在一个 空位 时才能向 左 移动，而片段 'R' 只有在其右侧直接存在一个 
空位 时才能向 右 移动。
字符 '_' 表示可以被 任意 'L' 或 'R' 片段占据的空位。
如果在移动字符串 start 中的片段任意次之后可以得到字符串 target ，返回 true ；否则，返回 false 。 

示例 1：
输入：start = "_L__R__R_", target = "L______RR"
输出：true
解释：可以从字符串 start 获得 target ，需要进行下面的移动：
- 将第一个片段向左移动一步，字符串现在变为 "L___R__R_" 。
- 将最后一个片段向右移动一步，字符串现在变为 "L___R___R" 。
- 将第二个片段向右移动三步，字符串现在变为 "L______RR" 。
可以从字符串 start 得到 target ，所以返回 true 。

示例 2：
输入：start = "R_L_", target = "__LR"
输出：false
解释：字符串 start 中的 'R' 片段可以向右移动一步得到 "_RL_" 。
但是，在这一步之后，不存在可以移动的片段，所以无法从字符串 start 得到 target 。

示例 3：
输入：start = "_R", target = "R_"
输出：false
解释：字符串 start 中的片段只能向右移动，所以无法从字符串 start 得到 target 。
"""
"""
思路：替换操作实际上是将 L 往左移动（L 左边为 _ 时才能移动），R 往右移动（R 右边是 _ 时才能移动），但 L 无法穿过 R。所以，如果
去掉 start 和 target 中的所有 _，剩下的字符应该是相同的，否则返回 false。
我们使用双指针 i 和 j 从头到尾遍历 start 和 target：
    如果当前字符为 L 且 i<j，那么这个 L 无法向右移动，返回 false；
    如果当前字符为 R 且 i>j，那么这个 R 无法向左移动，返回 false。
如果双指针均遍历到末尾，返回 true。
"""


class Solution:
    @staticmethod
    def canChange(start: str, target: str) -> bool:
        n = len(start)
        i = j = 0
        while 1:
            while i < n and start[i] == '_':
                i += 1
            while j < n and target[j] == '_':
                j += 1
            if i >= n and j >= n:
                return True
            if i >= n or j >= n or start[i] != target[j]:
                return False
            if start[i] == 'L' and i < j:
                return False
            if start[i] == 'R' and i > j:
                return False
            i, j = i + 1, j + 1

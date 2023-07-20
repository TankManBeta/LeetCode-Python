# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/7/19 23:35
"""
from typing import List

"""
机器人在一个无限大小的 XY 网格平面上行走，从点 (0, 0) 处开始出发，面向北方。该机器人可以接收以下三种类型的命令 commands ：
    -2 ：向左转 90 度
    -1 ：向右转 90 度
    1 <= x <= 9 ：向前移动 x 个单位长度
在网格上有一些格子被视为障碍物 obstacles 。第 i 个障碍物位于网格点  obstacles[i] = (xi, yi) 。
机器人无法走到障碍物上，它将会停留在障碍物的前一个网格方块上，但仍然可以继续尝试进行该路线的其余部分。
返回从原点到机器人所有经过的路径点（坐标为整数）的最大欧式距离的平方。（即，如果距离为 5 ，则返回 25 ）

注意：
北表示 +Y 方向。
东表示 +X 方向。
南表示 -Y 方向。
西表示 -X 方向。
"""
"""
思路：我们定义一个长度为 5 的方向数组 dirs=[0,1,0,−1,0]，数组中的相邻两个元素表示一个方向。即 (dirs[0],dirs[1]) 表示向北，而 
(dirs[1],dirs[2]) 表示向东，以此类推。我们使用一个哈希表 s 来存储所有障碍物的坐标，这样可以在 O(1) 的时间内判断下一步是否会
遇到障碍物。另外，使用两个变量 x 和 y 来表示机器人当前所在的坐标，初始时 x=y=0。变量 k 表示机器人当前的方向，答案变量 ans 表示
机器人距离原点的最大欧式距离的平方。接下来，我们遍历数组 commands 中的每个元素 c：如果 c=−2，表示机器人向左转 90 度，
即 k=(k+3)mod4；如果 c=−1，表示机器人向右转 90 度，即 k=(k+1)mod4；否则，表示机器人向前移动 c 个单位长度。我们将机器人当前的
方向 k 与方向数组 dirs 结合，即可得到机器人在 x 轴和 y 轴上的增量。我们将 c 个单位长度的增量分别累加到 x 和 y 上，并判断每次
移动后的新坐标 (nx,ny) 是否在障碍物的坐标中，如果不在，则更新答案 ans，否则停止模拟，进行下一条指令的模拟。最后返回答案 ans 即可。
"""


class Solution:
    @staticmethod
    def robotSim(commands: List[int], obstacles: List[List[int]]) -> int:
        dirs = (0, 1, 0, -1, 0)
        s = {(x, y) for x, y in obstacles}
        ans = k = 0
        x = y = 0
        for c in commands:
            if c == -2:
                k = (k + 3) % 4
            elif c == -1:
                k = (k + 1) % 4
            else:
                for _ in range(c):
                    nx, ny = x + dirs[k], y + dirs[k + 1]
                    if (nx, ny) in s:
                        break
                    x, y = nx, ny
                    ans = max(ans, x * x + y * y)
        return ans

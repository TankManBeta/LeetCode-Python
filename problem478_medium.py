"""
给定圆的半径和圆心的位置，实现函数 randPoint ，在圆中产生均匀随机点。
实现Solution类:
Solution(double radius, double x_center, double y_center)用圆的半径radius和圆心的位置 (x_center, y_center) 初始化对象
randPoint()返回圆内的一个随机点。圆周上的一点被认为在圆内。答案作为数组返回 [x, y] 。

输入:
["Solution","randPoint","randPoint","randPoint"]
[[1.0, 0.0, 0.0], [], [], []]
输出: [null, [-0.02493, -0.38077], [0.82314, 0.38945], [0.36572, 0.17248]]
解释:
Solution solution = new Solution(1.0, 0.0, 0.0);
solution.randPoint ();//返回[-0.02493，-0.38077]
solution.randPoint ();//返回[0.82314,0.38945]
solution.randPoint ();//返回[0.36572,0.17248]
"""
import random
from typing import List

"""
思路：均匀分布中采样，判别生成的点是否在圆内即可
"""


class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x = x_center
        self.y = y_center

    def randPoint(self) -> List[float]:
        while True:
            x, y = random.uniform(-self.radius, self.radius), random.uniform(-self.radius, self.radius)
            if x * x + y * y <= self.radius * self.radius:
                return [self.x + x, self.y + y]


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()

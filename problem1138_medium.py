# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/2/12 13:37
"""
"""
我们从一块字母板上的位置 (0, 0) 出发，该坐标对应的字符为 board[0][0]。
在本题里，字母板为board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]，如下所示。
我们可以按下面的指令规则行动：
    如果方格存在，'U' 意味着将我们的位置上移一行；
    如果方格存在，'D' 意味着将我们的位置下移一行；
    如果方格存在，'L' 意味着将我们的位置左移一列；
    如果方格存在，'R' 意味着将我们的位置右移一列；
    '!' 会把在我们当前位置 (r, c) 的字符 board[r][c] 添加到答案中。
（注意，字母板上只存在有字母的位置。）
返回指令序列，用最小的行动次数让答案和目标 target 相同。你可以返回任何达成目标的路径。

示例 1：
输入：target = "leet"
输出："DDR!UURRR!!DDD!"

示例 2：
输入：target = "code"
输出："RR!DDRR!UUL!R!"
"""
"""
思路：直接模拟，优先遵循向左向上的走法，可以避免z的坑
"""


class Solution:
    @staticmethod
    def alphabetBoardPath(target: str) -> str:
        i = j = 0
        ans = []
        for c in target:
            v = ord(c) - ord("a")
            x, y = v // 5, v % 5
            while j > y:
                j -= 1
                ans.append("L")
            while i > x:
                i -= 1
                ans.append("U")
            while j < y:
                j += 1
                ans.append("R")
            while i < x:
                i += 1
                ans.append("D")
            ans.append("!")
        return "".join(ans)

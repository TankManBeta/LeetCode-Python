# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/5/14 19:00
"""
from collections import Counter, deque

"""
我们有 n 种不同的贴纸。每个贴纸上都有一个小写的英文单词。
您想要拼写出给定的字符串 target ，方法是从收集的贴纸中切割单个字母并重新排列它们。如果你愿意，你可以多次使用每个贴纸，
每个贴纸的数量是无限的。
返回你需要拼出 target 的最小贴纸数量。如果任务不可能，则返回 -1 。
注意：在所有的测试用例中，所有的单词都是从 1000 个最常见的美国英语单词中随机选择的，并且 target 被选择为两个随机单词的连接。

输入： stickers = ["with","example","science"], target = "thehat"
输出：3
解释：
我们可以使用 2 个 "with" 贴纸，和 1 个 "example" 贴纸。
把贴纸上的字母剪下来并重新排列后，就可以形成目标 “thehat“ 了。
此外，这是形成目标字符串所需的最小贴纸数量。

输入：stickers = ["notice","possible"], target = "basicbasic"
输出：-1
解释：我们不能通过剪切给定贴纸的字母来形成目标“basicbasic”。
"""
"""
思路：从target出发【起始状态】，使用每个贴纸去掉对应个数的字母【状态转移】，看最终能否出现空字符串【目标状态】。优化: 优先从左
往右去掉当前状态中的字符，减少排列组合情况。(比如我们删1次stickers[0]同时删1次stickers[1]，就有两个顺序达到同样的效果)【大白话
就是先删a后删b，和先删b后删a一样，我们在乎的是选了ab，而不是排列ab】
"""


class Solution(object):
    def minStickers(self, stickers, target):
        """
        :type stickers: List[str]
        :type target: str
        :rtype: int
        """
        def trans(s):
            cnts = Counter()
            for c in s:
                if c in target:
                    cnts[c] += 1
            return cnts

        availables = [trans(st) for st in stickers]
        queue = deque([(target, 0)])
        explored = {target}
        while queue:
            cur, step = queue.popleft()
            if not cur:
                return step
            for avl in availables:
                if cur[0] in avl:
                    nxt = cur
                    for k, v in avl.items():
                        nxt = nxt.replace(k, '', v)
                    if nxt not in explored:
                        explored.add(nxt)
                        queue.append((nxt, step + 1))
        return -1

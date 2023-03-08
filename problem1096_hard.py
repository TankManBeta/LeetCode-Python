# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/3/7 22:29
"""
from typing import List

"""
如果你熟悉 Shell 编程，那么一定了解过花括号展开，它可以用来生成任意字符串。
花括号展开的表达式可以看作一个由 花括号、逗号 和 小写英文字母 组成的字符串，定义下面几条语法规则：
    如果只给出单一的元素 x，那么表达式表示的字符串就只有 "x"。R(x) = {x}
        例如，表达式 "a" 表示字符串 "a"。
        而表达式 "w" 就表示字符串 "w"。
    当两个或多个表达式并列，以逗号分隔，我们取这些表达式中元素的并集。R({e_1,e_2,...}) = R(e_1) ∪ R(e_2) ∪ ...
        例如，表达式 "{a,b,c}" 表示字符串 "a","b","c"。
        而表达式 "{{a,b},{b,c}}" 也可以表示字符串 "a","b","c"。
    要是两个或多个表达式相接，中间没有隔开时，我们从这些表达式中各取一个元素依次连接形成字符串。R(e_1 + e_2) = {a + b for (a, b) in R(e_1) × R(e_2)}
        例如，表达式 "{a,b}{c,d}" 表示字符串 "ac","ad","bc","bd"。
    表达式之间允许嵌套，单一元素与表达式的连接也是允许的。
        例如，表达式 "a{b,c,d}" 表示字符串 "ab","ac","ad"​​​​​​。
        例如，表达式 "a{b,c}{d,e}f{g,h}" 可以表示字符串 "abdfg", "abdfh", "abefg", "abefh", "acdfg", "acdfh", "acefg", "acefh"。
给出表示基于给定语法规则的表达式 expression，返回它所表示的所有字符串组成的有序列表。
假如你希望以「集合」的概念了解此题，也可以通过点击 “显示英文描述” 获取详情。 

示例 1：
输入：expression = "{a,b}{c,{d,e}}"
输出：["ac","ad","ae","bc","bd","be"]

示例 2：
输入：expression = "{{a,z},a{b,c},{ab,z}}"
输出：["a","ab","ac","z"]
解释：输出中 不应 出现重复的组合结果。
"""
"""
思路：递归。我们设计一个递归函数 dfs(exp)，用于处理表达式 exp，并将结果存入集合 s 中。对于表达式 exp，我们首先找到第一个
右花括号的位置 j，如果找不到，说明 exp 中没有右花括号，即 exp 为单一元素，直接将 exp 加入集合 s 中即可。否则，我们从位置 j 
开始往左找到第一个左花括号的位置 i，此时 exp[:i] 和 exp[j+1:] 分别为 exp 的前缀和后缀，记为 a 和 c。而 exp[i+1:j] 为 exp 
中花括号内的部分，即 exp 中的子表达式，我们将其按照逗号分割成多个字符串 b1,b2,⋯,bk ，然后对每个 bi，我们将 a+bi+c 拼接成
新的表达式，递归调用 dfs 函数处理新的表达式，即 dfs(a+bi+c)。最后，我们将集合 s 中的元素按照字典序排序，即可得到答案。
"""


class Solution:
    @staticmethod
    def braceExpansionII(expression: str) -> List[str]:
        def dfs(exp):
            j = exp.find('}')
            if j == -1:
                s.add(exp)
                return
            i = exp.rfind('{', 0, j - 1)
            a, c = exp[:i], exp[j + 1:]
            for b in exp[i + 1: j].split(','):
                dfs(a + b + c)
        s = set()
        dfs(expression)
        return sorted(s)

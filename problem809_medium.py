# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/11/25 20:55
"""
from typing import List

"""
有时候人们会用重复写一些字母来表示额外的感受，比如 "hello" -> "heeellooo", "hi" -> "hiii"。
我们将相邻字母都相同的一串字符定义为相同字母组，例如："h", "eee", "ll", "ooo"。
对于一个给定的字符串 S ，如果另一个单词能够通过将一些字母组扩张从而使其和 S 相同，我们将这个单词定义为可扩张的（stretchy）。
扩张操作定义如下：选择一个字母组（包含字母 c ），然后往其中添加相同的字母 c 使其长度达到 3 或以上。
例如，以 "hello" 为例，我们可以对字母组 "o" 扩张得到 "hellooo"，但是无法以同样的方法得到 "helloo" 因为字母组 "oo" 长度小于 3。
此外，我们可以进行另一种扩张 "ll" -> "lllll" 以获得 "helllllooo"。
如果 s = "helllllooo"，那么查询词 "hello" 是可扩张的，因为可以对它执行这两种扩张操作使得 query = "hello" -> "hellooo" -> "helllllooo" = s。
输入一组查询单词，输出其中可扩张的单词数量。

示例：
输入： 
s = "heeellooo"
words = ["hello", "hi", "helo"]
输出：1
解释：
我们能通过扩张 "hello" 的 "e" 和 "o" 来得到 "heeellooo"。
我们不能通过扩张 "helo" 来得到 "heeellooo" 因为 "ll" 的长度小于 3 。
"""
"""
我们可以遍历数组 words，对于数组中的每个单词 t，判断 t 是否可以通过扩张得到 s，如果可以，那么答案加一。
因此，问题的关键在于判断单词 t 是否可以通过扩张得到 s。这里我们通过一个 check(s,t) 函数来判断。函数的具体实现逻辑如下：
首先判断 s 和 t 的长度关系，如果 t 的长度大于 s，直接返回 false。否则，我们用双指针 i 和 j 分别指向 s 和 t，初始时 i 和 j 的值均为 0。
如果 i 和 j 指向的字符不同，那么 t 无法通过扩张得到 s，直接返回 false；否则，我们需要判断 i 指向的字符的连续出现次数 c1 
和 j 指向的字符的连续出现次数 c2 的关系。如果 c1<c2 或者 c1<3 并且 c1!=c2，那么 t 无法通过扩张得到 s，直接返回 false；
否则，将 i 和 j 分别右移 c1和 c2 次。继续判断。
如果 i 和 j 都到达了字符串的末尾，那么 t 可以通过扩张得到 s，返回 true，否则返回 false。
"""


class Solution:
    @staticmethod
    def expressiveWords(s: str, words: List[str]) -> int:
        def check(s, t):
            m, n = len(s), len(t)
            if n > m:
                return False
            i = j = 0
            while i < m and j < n:
                if s[i] != t[j]:
                    return False
                k = i
                while k < m and s[k] == s[i]:
                    k += 1
                c1 = k - i
                i, k = k, j
                while k < n and t[k] == t[j]:
                    k += 1
                c2 = k - j
                j = k
                if c1 < c2 or (c1 < 3 and c1 != c2):
                    return False
            return i == m and j == n

        return sum(check(s, t) for t in words)

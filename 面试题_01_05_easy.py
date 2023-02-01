# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/5/13 15:10
"""
"""
字符串有三种编辑操作:插入一个字符、删除一个字符或者替换一个字符。 给定两个字符串，编写一个函数判定它们是否只需要一次(或者零次)
编辑。

输入: 
first = "pale"
second = "ple"
输出: True

输入: 
first = "pales"
second = "pal"
输出: False
"""
"""
思路：首先判断两个是否长度相差2及以上，如果超过的话肯定不能一次转化成功，然后双指针遍历两个字符串，如果其中一个字符和另一个不相
等，如果两个字符串长度相同，则看i+1后和j+1以后的是否相同；如果两个字符串长度不相同，则看i+1和j之后的是否相同，因为在j的位置插入
新的字符
"""


class Solution(object):
    def oneEditAway(self, first, second):
        """
        :type first: str
        :type second: str
        :rtype: bool
        """
        m, n = len(first), len(second)
        if m < n:
            return self.oneEditAway(second, first)
        if m - n > 1:
            return False
        for i, (x, y) in enumerate(zip(first, second)):
            if x != y:
                return first[i + 1:] == second[i + 1:] if m == n else first[i + 1:] == second[i:]
        return True

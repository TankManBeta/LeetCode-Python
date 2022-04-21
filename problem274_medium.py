# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/4/20 11:08
"""
"""
给你一个整数数组 citations ，其中 citations[i] 表示研究者的第 i 篇论文被引用的次数。计算并返回该研究者的 h 指数。根据维基百科
上 h 指数的定义：h 代表“高引用次数”，一名科研人员的 h指数是指他（她）的 （n 篇论文中）总共有 h 篇论文分别被引用了至少 h 次。
且其余的 n - h 篇论文每篇被引用次数 不超过 h 次。
如果 h 有多种可能的值，h 指数 是其中最大的那个。

输入：citations = [3,0,6,1,5]
输出：3 
解释：给定数组表示研究者总共有 5 篇论文，每篇论文相应的被引用了 3, 0, 6, 1, 5 次。
     由于研究者有 3 篇论文每篇 至少 被引用了 3 次，其余两篇论文每篇被引用 不多于 3 次，所以她的 h 指数是 3。

输入：citations = [1,3,1]
输出：1
"""
"""
思路：
（1）排序，首先我们可以将初始的 H 指数 h 设为 0，然后将引用次数排序，并且对排序后的数组从大到小遍历。根据 H 指数的定义，
如果当前 H 指数为 h 并且在遍历过程中找到当前值 citations[i]>h，则说明我们找到了一篇被引用了至少 h+1 次的论文，
所以将现有的 h 值加 1。继续遍历直到 h 无法继续增大。最后返回 h 作为最终答案。
（2）计数排序，新建并维护一个数组 counter 用来记录当前引用次数的论文有几篇。根据定义，我们可以发现H指数不可能大于总的论文发表数，
所以对于引用次数超过论文发表数的情况，我们可以将其按照总的论文发表数来计算即可。这样我们可以限制参与排序的数的大小为 [0,n]
（其中 n 为总的论文发表数），使得计数排序的时间复杂度降低到O(n)。最后我们可以从后向前遍历数组 counter，对于每个 0≤i≤n，
在数组 counter 中得到大于或等于当前引用次数 i 的总论文数。当我们找到一个 H 指数时跳出循环，并返回结果。
"""


class Solution(object):
    @staticmethod
    def hIndex(citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        # sorted_citation = sorted(citations, reverse = True)
        # h = 0; i = 0; n = len(citations)
        # while i < n and sorted_citation[i] > h:
        #     h += 1
        #     i += 1
        # return h

        n = len(citations)
        tot = 0
        counter = [0] * (n+1)
        for c in citations:
            if c >= n:
                counter[n] += 1
            else:
                counter[c] += 1
        for i in range(n, -1, -1):
            tot += counter[i]
            if tot >= i:
                return i
        return 0

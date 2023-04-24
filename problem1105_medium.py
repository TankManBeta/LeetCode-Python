# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/4/23 10:48
"""
from typing import List

"""
给定一个数组 books ，其中 books[i] = [thicknessi, heighti] 表示第 i 本书的厚度和高度。你也会得到一个整数 shelfWidth 。
按顺序 将这些书摆放到总宽度为 shelfWidth 的书架上。
先选几本书放在书架上（它们的厚度之和小于等于书架的宽度 shelfWidth ），然后再建一层书架。重复这个过程，直到把所有的书都放在书架上。
需要注意的是，在上述过程的每个步骤中，摆放书的顺序与你整理好的顺序相同。
    例如，如果这里有 5 本书，那么可能的一种摆放情况是：第一和第二本书放在第一层书架上，第三本书放在第二层书架上，第四和第五本书
    放在最后一层书架上。
每一层所摆放的书的最大高度就是这一层书架的层高，书架整体的高度为各层高之和。
以这种方式布置书架，返回书架整体可能的最小高度。 

示例 1：
输入：books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], shelfWidth = 4
输出：6
解释：
3 层书架的高度和为 1 + 3 + 2 = 6 。
第 2 本书不必放在第一层书架上。

示例 2:
输入: books = [[1,3],[2,4],[3,2]], shelfWidth = 6
输出: 4
"""
"""
思路：动态规划，我们定义f[i]为放下前i本书需要的最小高度，初始f[0]=0，答案即为f[n]。对于f[i]，它的最后一本书是books[i-1]。对于
books[i-1]，我们有两种处理办法，第一种是将它放入新的一层，则f[i]=f[i-1]+h；另一种办法是将它和已经有的最后基本放在同一层书架，
所以我们枚举books[i-1]前面的书，累加w，直到w超过shelfWidth，表示当前层不能再放书，更新当前层的最大高度 h=max(h,books[j−1][1])，
那么此时有 f[i]=min(f[i],f[j−1]+h)。
"""


class Solution:
    @staticmethod
    def minHeightShelves(books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        f = [0] * (n + 1)
        for i, (w, h) in enumerate(books, 1):
            f[i] = f[i - 1] + h
            for j in range(i - 1, 0, -1):
                w += books[j - 1][0]
                if w > shelfWidth:
                    break
                h = max(h, books[j - 1][1])
                f[i] = min(f[i], f[j - 1] + h)
        return f[n]

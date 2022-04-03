# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/4/2 23:31
"""
"""
找出所有相加之和为 n 的 k 个数的组合，且满足下列条件：
    只使用数字1到9
    每个数字 最多使用一次 
返回 所有可能的有效组合的列表 。该列表不能包含相同的组合两次，组合可以以任何顺序返回。

输入: k = 3, n = 7
输出: [[1,2,4]]
解释:
1 + 2 + 4 = 7
没有其他符合的组合了。

输入: k = 3, n = 9
输出: [[1,2,6], [1,3,5], [2,3,4]]
解释:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
没有其他符合的组合了。

输入: k = 4, n = 1
输出: []
解释: 不存在有效的组合。
在[1,9]范围内使用4个不同的数字，我们可以得到的最小和是1+2+3+4 = 10，因为10 > 1，没有有效的组合。
"""
"""
思路：
（1）dfs
（2）二进制枚举，一共有1<<9种情况，然后判断这么多中情况中的每一个情况哪些数被用过，记录被用的数，如果长度和需要的数字个数不相同，则说明不可以，否则判断和是否等于target
"""

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        # combination = list()
        # combinations = list()
        # def dfs(count):
        #     if count == k:
        #         if sum(combination)==n:
        #             if sorted(combination) not in combinations:
        #                 combinations.append(combination[::])
        #         return
        #     for num in range(1,10):
        #         if num not in combination:
        #             combination.append(num)
        #             dfs(count+1)
        #             combination.pop()

        # dfs(0)
        # return combinations

        self.k = k
        self.n = n
        self.combination = list()
        self.combinations = list()
        def check(mask, length, total):
            self.combination = list()
            for i in range(9):
                if ((1<<i)&mask)!=0:
                    self.combination.append(i+1)
            if len(self.combination) != length:
                return False
            sum = 0
            for num in self.combination:
                sum += num
            return total == sum
        for mask in range(0, 1<<9):
            if check(mask, k, n):
                self.combinations.append(self.combination[::])
        return self.combinations
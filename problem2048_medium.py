# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/12/8 16:20
"""
"""
如果整数  x 满足：对于每个数位 d ，这个数位 恰好 在 x 中出现 d 次。那么整数 x 就是一个 数值平衡数 。
给你一个整数 n ，请你返回 严格大于 n 的 最小数值平衡数 。

示例 1：
输入：n = 1
输出：22
解释：
22 是一个数值平衡数，因为：
- 数字 2 出现 2 次 
这也是严格大于 1 的最小数值平衡数。

示例 2：
输入：n = 1000
输出：1333
解释：
1333 是一个数值平衡数，因为：
- 数字 1 出现 1 次。
- 数字 3 出现 3 次。 
这也是严格大于 1000 的最小数值平衡数。
注意，1022 不能作为本输入的答案，因为数字 0 的出现次数超过了 0 。

示例 3：
输入：n = 3000
输出：3133
解释：
3133 是一个数值平衡数，因为：
- 数字 1 出现 1 次。
- 数字 3 出现 3 次。 
这也是严格大于 3000 的最小数值平衡数。
"""
"""
思路：从n+1开始，判断每一个数是否是平衡数即可。判断的时候用数组，因为范围是10**6，所以肯定不可能出现8和9，然后出现0的话也不行。
"""


class Solution:
    @staticmethod
    def nextBeautifulNumber(n: int) -> int:
        def is_beautiful(num):
            count = [0] * 8
            while num != 0:
                if num % 10 > 7 or num % 10 == 0:
                    return False
                count[num % 10] += 1
                num //= 10
            for i in range(1, 8):
                if count[i] and count[i] != i:
                    return False
            return True

        for j in range(n + 1, 10 ** 8):
            if is_beautiful(j):
                return j

# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/2/23 10:33
"""
from typing import List

"""
给你两个整数 n 和 start。你的任务是返回任意 (0,1,2,,...,2^n-1) 的排列 p，并且满足：
    p[0] = start
    p[i] 和 p[i+1] 的二进制表示形式只有一位不同
    p[0] 和 p[2^n -1] 的二进制表示形式也只有一位不同

示例 1：
输入：n = 2, start = 3
输出：[3,2,0,1]
解释：这个排列的二进制表示是 (11,10,00,01)
     所有的相邻元素都有一位是不同的，另一个有效的排列是 [3,1,0,2]
     
示例 2：
输出：n = 3, start = 2
输出：[2,6,7,5,4,0,1,3]
解释：这个排列的二进制表示是 (010,110,111,101,100,000,001,011)
"""
"""
思路：
（1）归纳法。本题和格雷编码类似，不同点是本题从start开始，只要每个数和start做异或即可
（2）二进制码转换成二进制格雷码，其法则是保留二进制码的最高位作为格雷码的最高位，而次高位格雷码为二进制码的高位与次高位相异或，
而格雷码其余各位与次高位的求法相类似。由于 gray(0)=0，那么 gray(0)⊕start=start，而 gray(i) 与 gray(i−1) 只有一个二进制位不同，
所以 gray(i)⊕start 与 gray(i−1)⊕start 也只有一个二进制位不同。因此，我们也可以直接将 [0,..2^n−1] 这些整数转换成对应的 
gray(i)⊕start，即可得到首项为 start 的格雷码排列。
"""


class Solution:
    @staticmethod
    def circularPermutation(n: int, start: int) -> List[int]:
        # ans = [start]
        # for i in range(1, n + 1):
        #     for j in range(len(ans) - 1, -1, -1):
        #         ans.append(((ans[j] ^ start) | (1 << (i - 1))) ^ start)
        # return ans

        return [i ^ (i >> 1) ^ start for i in range(1 << n)]

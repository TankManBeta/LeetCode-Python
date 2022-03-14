# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/3/13 15:35
"""
"""
给定一个表示数据的整数数组 data ，返回它是否为有效的 UTF-8 编码。
UTF-8 中的一个字符可能的长度为 1 到 4 字节，遵循以下的规则：
    对于 1 字节 的字符，字节的第一位设为 0 ，后面 7 位为这个符号的 unicode 码。
    对于 n 字节 的字符 (n > 1)，第一个字节的前 n 位都设为1，第 n+1 位设为 0 ，后面字节的前两位一律设为 10 。
    剩下的没有提及的二进制位，全部为这个符号的 unicode 码。

输入：data = [197,130,1]
输出：true
解释：数据表示字节序列:11000101 10000010 00000001。
这是有效的 utf-8 编码，为一个 2 字节字符，跟着一个 1 字节字符。

输入：data = [235,140,4]
输出：false
解释：数据表示 8 位的序列: 11101011 10001100 00000100.
前 3 位都是 1 ，第 4 位为 0 表示它是一个 3 字节字符。
下一个字节是开头为 10 的延续字节，这是正确的。
但第二个延续字节不以 10 开头，所以是不符合规则的。
"""
"""
思路：直接模拟，如果&(1<<7)等于0就继续，否则说明是多字节，记录前面1的个数，如果小于2或大于4就是非法，然后再判断剩下的是否是10
开头即可
"""


class Solution(object):
    @staticmethod
    def valid_utf8(data):
        """
        :type data: List[int]
        :rtype: bool
        """
        index = 0
        n = len(data)
        mask1, mask2 = 1 << 7, (1 << 7) | (1 << 6)
        while index < n:
            if data[index] & mask1 == 0:
                index += 1
                continue
            else:
                count, temp_mask = 0, mask1
                while data[index] & temp_mask:
                    count += 1
                    temp_mask >>= 1
                if count > 4 or count < 2:
                    return False
                if index + count > n or any((ch & mask2) != mask1 for ch in data[index + 1: index + count]):
                    return False
                index += count
        return True

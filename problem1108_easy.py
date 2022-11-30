"""
给你一个有效的 IPv4 地址address，返回这个 IP 地址的无效化版本。
所谓无效化IP 地址，其实就是用"[.]"代替了每个 "."。

输入：address = "1.1.1.1"
输出："1[.]1[.]1[.]1"

输入：address = "255.100.50.0"
输出："255[.]100[.]50[.]0"
"""
"""
思路：直接replace即可
"""


class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')
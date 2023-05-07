# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/5/6 21:07
"""
"""
给你一个字符串 croakOfFrogs，它表示不同青蛙发出的蛙鸣声（字符串 "croak" ）的组合。由于同一时间可以有多只青蛙呱呱作响，
所以 croakOfFrogs 中会混合多个 “croak” 。
请你返回模拟字符串中所有蛙鸣所需不同青蛙的最少数目。
要想发出蛙鸣 "croak"，青蛙必须 依序 输出 ‘c’, ’r’, ’o’, ’a’, ’k’ 这 5 个字母。如果没有输出全部五个字母，那么它就不会发出声音。
如果字符串 croakOfFrogs 不是由若干有效的 "croak" 字符混合而成，请返回 -1 。 

示例 1：
输入：croakOfFrogs = "croakcroak"
输出：1 
解释：一只青蛙 “呱呱” 两次

示例 2：
输入：croakOfFrogs = "crcoakroak"
输出：2 
解释：最少需要两只青蛙，“呱呱” 声用黑体标注
第一只青蛙 "crcoakroak"
第二只青蛙 "crcoakroak"

示例 3：
输入：croakOfFrogs = "croakcrook"
输出：-1
解释：给出的字符串不是 "croak" 的有效组合。
"""
"""
思路：我们遍历字符串 croakOfFrogs 中的每个字母 c，找到 c 对应的下标 i，然后将 cnt[i] 加 1。接下来，根据 i 值的不同，我们分别
进行如下操作：
    如果 i=0，那么当前有一个新的青蛙开始蛙鸣，因此令 x 的值加 1，然后我们更新 ans=max(ans,x)；
    否则，如果 cnt[i−1]=0，那么表示当前没有青蛙可以发出字母 c，无法完成蛙鸣，返回 −1，否则我们令 cnt[i−1] 减 1。如果 i=4，
    那么表示青蛙已经完成了一个蛙鸣，因此令 x 的值减 1。遍历结束后，如果 x=0，那么说明青蛙已经完成了所有的蛙鸣，返回 ans，
    否则返回 −1。
"""


class Solution:
    @staticmethod
    def minNumberOfFrogs(croakOfFrogs: str) -> int:
        if len(croakOfFrogs) % 5 != 0:
            return -1
        idx = {c: i for i, c in enumerate('croak')}
        cnt = [0] * 5
        ans = x = 0
        for i in map(idx.get, croakOfFrogs):
            cnt[i] += 1
            if i == 0:
                x += 1
                ans = max(ans, x)
            else:
                if cnt[i - 1] == 0:
                    return -1
                cnt[i - 1] -= 1
                if i == 4:
                    x -= 1
        return -1 if x else ans

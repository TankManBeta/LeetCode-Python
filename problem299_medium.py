# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/12/16 12:16
"""
"""
你在和朋友一起玩 猜数字（Bulls and Cows）游戏，该游戏规则如下：
写出一个秘密数字，并请朋友猜这个数字是多少。朋友每猜测一次，你就会给他一个包含下述信息的提示：
    猜测数字中有多少位属于数字和确切位置都猜对了（称为 "Bulls"，公牛），
    有多少位属于数字猜对了但是位置不对（称为 "Cows"，奶牛）。也就是说，这次猜测中有多少位非公牛数字可以通过重新排列转换成公牛数字。
给你一个秘密数字 secret 和朋友猜测的数字 guess ，请你返回对朋友这次猜测的提示。
提示的格式为 "xAyB" ，x 是公牛个数， y 是奶牛个数，A 表示公牛，B 表示奶牛。
请注意秘密数字和朋友猜测的数字都可能含有重复数字。

示例 1：
输入：secret = "1807", guess = "7810"
输出："1A3B"
解释：数字和位置都对（公牛）用 '|' 连接，数字猜对位置不对（奶牛）的采用斜体加粗标识。
"1807"
  |
"7810"

示例 2：
输入：secret = "1123", guess = "0111"
输出："1A1B"
解释：数字和位置都对（公牛）用 '|' 连接，数字猜对位置不对（奶牛）的采用斜体加粗标识。
"1123"        "1123"
  |      or     |
"0111"        "0111"
注意，两个不匹配的 1 中，只有一个会算作奶牛（数字猜对位置不对）。通过重新排列非公牛数字，其中仅有一个 1 可以成为公牛数字。
"""
"""
思路：遍历，如果guess[i]==secret[i]，说明该位置正确；如果不等说明该位置不正确，统计一下secret和guess中还未正确匹配的数字的数量，
最后取两者之间的最小值即可。（自己的思路也是如此，但是太麻烦了）
"""


class Solution:
    @staticmethod
    def getHint(secret: str, guess: str) -> str:
        # bull, cow = 0, 0
        # n = len(secret)
        # visited = [False] * n
        # count = defaultdict(int)
        # for i in range(n):
        #     if secret[i] == guess[i]:
        #         bull += 1
        #         visited[i] = True
        #     else:
        #         count[guess[i]] += 1
        # for i in range(n):
        #     if not visited[i]:
        #         already = count[secret[i]]
        #         if already > 0:
        #             cow += 1
        #             count[secret[i]] = already - 1
        # return f"{bull}A{cow}B"

        bull = 0
        n = len(secret)
        count_secret, count_guess = [0] * 10, [0] * 10
        for i in range(n):
            if guess[i] == secret[i]:
                bull += 1
            else:
                count_secret[int(secret[i])] += 1
                count_guess[int(guess[i])] += 1
        cow = sum([min(count_secret[i], count_guess[i]) for i in range(10)])
        return f"{bull}A{cow}B"

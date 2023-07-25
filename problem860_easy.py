# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/7/22 12:40
"""
from typing import List

"""
在柠檬水摊上，每一杯柠檬水的售价为 5 美元。顾客排队购买你的产品，（按账单 bills 支付的顺序）一次购买一杯。
每位顾客只买一杯柠檬水，然后向你付 5 美元、10 美元或 20 美元。你必须给每个顾客正确找零，也就是说净交易是每位顾客向你支付 5 美元。
注意，一开始你手头没有任何零钱。
给你一个整数数组 bills ，其中 bills[i] 是第 i 位顾客付的账。如果你能给每位顾客正确找零，返回 true ，否则返回 false 。 

示例 1：
输入：bills = [5,5,5,10,20]
输出：true
解释：
前 3 位顾客那里，我们按顺序收取 3 张 5 美元的钞票。
第 4 位顾客那里，我们收取一张 10 美元的钞票，并返还 5 美元。
第 5 位顾客那里，我们找还一张 10 美元的钞票和一张 5 美元的钞票。
由于所有客户都得到了正确的找零，所以我们输出 true。

示例 2：
输入：bills = [5,5,10,10,20]
输出：false
解释：
前 2 位顾客那里，我们按顺序收取 2 张 5 美元的钞票。
对于接下来的 2 位顾客，我们收取一张 10 美元的钞票，然后返还 5 美元。
对于最后一位顾客，我们无法退回 15 美元，因为我们现在只有两张 10 美元的钞票。
由于不是每位顾客都得到了正确的找零，所以答案是 false。
"""
"""
思路：如果是 5 美元，那么直接收下即可；如果是 10 美元，那么需要找零 5 美元；如果是 20 美元，那么需要找零 15 美元，此时有两种
找零方式：找零 1 张 10 美元 + 1 张 5 美元；找零 3 张 5 美元。我们优先用第一种找零方式，如果没有足够的 10 美元，那么用第二种方式；
如果发现 5 美元的数量不够，直接返回 false。
"""


class Solution:
    @staticmethod
    def lemonadeChange(bills: List[int]) -> bool:
        five, ten, twenty = 0, 0, 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if five > 0:
                    five -= 1
                    ten += 1
                else:
                    return False
            else:
                flag = False
                if ten > 0:
                    if five > 0:
                        five -= 1
                        ten -= 1
                        twenty += 1
                        flag = True
                else:
                    if five >= 3:
                        five -= 3
                        twenty += 1
                        flag = True
                if flag:
                    continue
                else:
                    return False
        return True

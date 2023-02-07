# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/2/7 22:19
"""
from collections import defaultdict
from typing import List

"""
力扣公司的员工都使用员工卡来开办公室的门。每当一个员工使用一次他的员工卡，安保系统会记录下员工的名字和使用时间。
如果一个员工在一小时时间内使用员工卡的次数大于等于三次，这个系统会自动发布一个 警告 。
给你字符串数组 keyName 和 keyTime ，其中 [keyName[i], keyTime[i]] 对应一个人的名字和他在 某一天 内使用员工卡的时间。
使用时间的格式是 24小时制 ，形如 "HH:MM" ，比方说 "23:51" 和 "09:49" 。
请你返回去重后的收到系统警告的员工名字，将它们按 字典序升序 排序后返回。
请注意 "10:00" - "11:00" 视为一个小时时间范围内，而 "23:51" - "00:10" 不被视为一小时内，因为系统记录的是某一天内的使用情况。

示例 1：
输入：keyName = ["daniel","daniel","daniel","luis","luis","luis","luis"], keyTime = ["10:00","10:40","11:00","09:00","11:00","13:00","15:00"]
输出：["daniel"]
解释："daniel" 在一小时内使用了 3 次员工卡（"10:00"，"10:40"，"11:00"）。

示例 2：
输入：keyName = ["alice","alice","alice","bob","bob","bob","bob"], keyTime = ["12:01","12:00","18:00","21:00","21:20","21:30","23:00"]
输出：["bob"]
解释："bob" 在一小时内使用了 3 次员工卡（"21:00"，"21:20"，"21:30"）。

示例 3：
输入：keyName = ["john","john","john"], keyTime = ["23:58","23:59","00:01"]
输出：[]

示例 4：
输入：keyName = ["leslie","leslie","leslie","clare","clare","clare","clare"], keyTime = ["13:00","13:20","14:00","18:00","18:51","19:30","19:49"]
输出：["clare","leslie"]
"""
"""
思路：对于每一个员工，把记录的时间换成分钟记录下来，然后对这些分钟进行排序，如果发现列表中存在三个连续元素中的最大元素与最小
元素之差不超过 60，即意味着这三次使用员工卡是在一小时之内发生的，因此因此该员工会收到系统警告。
"""


class Solution:
    @staticmethod
    def alertNames(keyName: List[str], keyTime: List[str]) -> List[str]:
        counter = defaultdict(list)
        for i, name in enumerate(keyName):
            hour = int(keyTime[i][:2])
            minute = int(keyTime[i][-2:])
            minutes = 60*hour + minute
            counter[name].append(minutes)
        ans = []
        for name, times in counter.items():
            times.sort()
            if any(t2 - t1 <= 60 for t1, t2 in zip(times, times[2:])):
                ans.append(name)
        ans.sort()
        return ans

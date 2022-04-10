# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/4/9 13:20
"""
"""
给定一个大小为 n 的整数数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。

输入：[3,2,3]
输出：[3]

输入：nums = [1]
输出：[1]

输入：[1,1,1,3,3,2,2,2]
输出：[1,2]
"""
"""
思路：我们每次检测当前元素是否为第一个选中的元素或者第二个选中的元素。每次我们发现当前元素与已经选中的两个元素都不相同，
则进行抵消一次。如果存在最终选票大于 00 的元素，我们还需要再次统计已选中元素的次数,检查元素的次数是否大于⌊n/3⌋ 
"""


class Solution(object):
    @staticmethod
    def majorityElement(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        element1, element2 = 0, 0
        vote1, vote2 = 0, 0
        for num in nums:
            # 如果该元素为第一个元素，则计数加1
            if vote1 > 0 and num == element1:
                vote1 += 1
            # 如果该元素为第二个元素，则计数加1
            elif vote2 > 0 and num == element2:
                vote2 += 1
            # 选择第一个元素
            elif vote1 == 0:
                element1 = num
                vote1 += 1
            # 选择第二个元素
            elif vote2 == 0:
                element2 = num
                vote2 += 1
            # 如果三个元素均不相同，则相互抵消1次
            else:
                vote1 -= 1
                vote2 -= 1
        cnt1, cnt2 = 0, 0
        for num in nums:
            if vote1 > 0 and num == element1:
                cnt1 += 1
            if vote2 > 0 and num == element2:
                cnt2 += 1
        # 检测元素出现的次数是否满足要求
        if vote1 > 0 and cnt1 > len(nums) / 3:
            ans.append(element1)
        if vote2 > 0 and cnt2 > len(nums) / 3:
            ans.append(element2)
        return ans

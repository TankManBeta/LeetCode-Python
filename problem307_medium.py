# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/4/4 16:10
"""
"""
给你一个数组 nums ，请你完成两类查询。
    其中一类查询要求 更新 数组 nums 下标对应的值
    另一类查询要求返回数组 nums 中索引 left 和索引 right 之间（ 包含 ）的nums元素的 和 ，其中 left <= right
实现 NumArray 类：
    NumArray(int[] nums) 用整数数组 nums 初始化对象
    void update(int index, int val) 将 nums[index] 的值 更新 为 val
    int sumRange(int left, int right) 返回数组 nums 中索引 left 和索引 right 之间（ 包含 ）的nums元素的 和 
    （即，nums[left] + nums[left + 1], ..., nums[right]）
    
输入：
["NumArray", "sumRange", "update", "sumRange"]
[[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
输出：
[null, 9, null, 8]
解释：
NumArray numArray = new NumArray([1, 3, 5]);
numArray.sumRange(0, 2); // 返回 1 + 3 + 5 = 9
numArray.update(1, 2);   // nums = [1,2,5]
numArray.sumRange(0, 2); // 返回 1 + 2 + 5 = 8
"""
"""
思路：
（1）暴力超时
（2）分块，分成n个size大小的块，每次更新nums和sums，取的时候就计算左右边界分别在哪一块，如果在一块种就直接返回nums中求和，否则是sum1+sum2+sum3
（3）树形数组，通过sums之间的组合可以获取到前缀和，通过lowbit算出最低位为1表示的数，更新时x+lowbit(x)获取下一步的下标，查询时x-lowbit(x)
"""


class NumArray(object):

    # def __init__(self, nums):
    #     """
    #     :type nums: List[int]
    #     """
    #     n = len(nums)
    #     size = int(n ** 0.5)
    #     sums = [0] * ((n + size - 1) // size)  # n/size 向上取整
    #     for i, num in enumerate(nums):
    #         sums[i // size] += num
    #     self.nums = nums
    #     self.sums = sums
    #     self.size = size

    # def update(self, index, val):
    #     """
    #     :type index: int
    #     :type val: int
    #     :rtype: None
    #     """
    #     self.sums[index // self.size] += val - self.nums[index]
    #     self.nums[index] = val

    # def sumRange(self, left, right):
    #     """
    #     :type left: int
    #     :type right: int
    #     :rtype: int
    #     """
    #     m = self.size
    #     b1, b2 = left // m, right // m
    #     if b1 == b2:  # 区间 [left, right] 在同一块中
    #         return sum(self.nums[left:right + 1])
    #     return sum(self.nums[left:(b1 + 1) * m]) + sum(self.sums[b1 + 1:b2]) + sum(self.nums[b2 * m:right + 1])

    def __init__(self, nums):
        self.nums = nums
        self.tree = [0] * (len(nums) + 1)
        for i, num in enumerate(nums, 1):
            self.add(i, num)

    def add(self, index, val):
        while index < len(self.tree):
            self.tree[index] += val
            index += index & -index

    def prefixSum(self, index):
        s = 0
        while index:
            s += self.tree[index]
            index &= index - 1
        return s

    def update(self, index, val):
        self.add(index + 1, val - self.nums[index])
        self.nums[index] = val

    def sumRange(self, left, right):
        return self.prefixSum(right + 1) - self.prefixSum(left)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)

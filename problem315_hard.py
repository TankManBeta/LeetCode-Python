# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/2/20 11:44
"""
from typing import List

"""
给你一个整数数组 nums ，按要求返回一个新数组 counts 。数组 counts 有该性质： counts[i] 的值是  nums[i] 右侧小于 nums[i] 的元素的数量。

示例 1：
输入：nums = [5,2,6,1]
输出：[2,1,1,0] 
解释：
5 的右侧有 2 个更小的元素 (2 和 1)
2 的右侧仅有 1 个更小的元素 (1)
6 的右侧有 1 个更小的元素 (1)
1 的右侧有 0 个更小的元素

示例 2：
输入：nums = [-1]
输出：[0]

示例 3：
输入：nums = [-1,-1]
输出：[0,0]
"""
"""
思路：
（1） 维护一个有序数组 sl，从右往左依次往里添加 nums 中的元素，每次添加 nums[i] 前基于「二分搜索」判断出当前 sl 中比 nums[i] 
小的元素个数（即 nums[i] 右侧比 nums[i] 还要小的元素个数），并计入答案即可。
（2）归并排序，我们将数组进行扩充，以便在位置发生改变之后进行重新定位。例如，对于 nums=[5,2,6,1]，我们将其扩充为 nums=[(5,0),
(2,1),(6,2),(1,3)]。这样在对 nums 进行排序的过程中，即便 nums 中元素的位置发生了变化，也可将每个元素贡献的逆序对数目准确定位
到对应的位置上。我们使用归并排序，使得 nums[low, mid] 和 nums[mid+1, high] 已排序好。在此基础之上统计逆序对即可，在双指针遍历 
nums[low, mid] 和 nums[mid+1, high] 的时候，如果前出现前半部分的数（下标为left）小于后半部分的数（下标为right），那么right
之前的数字个数就是逆序对数目，也就是右边比当前数小的个数。例如前半部分归并排序和后半部分归并排序的结果分别为[3,4,5,7]和[1,2,5,6]
前面遍历到3，后面遍历到5，右边比3小的数只有1，2，逆序对的数目就加2。
（3）树状数组，从右向左读取排名；先查询严格小于当前排名的「前缀和」，这里「前缀和」指的是，严格小于当前排名的元素的个数，这一步
对应「前缀和查询」；然后给「当前排名」加 1，这一步对应「单点更新」。更新排名的时候要连同自己的所有父节点都更新，因为根据树状数组
的定义，某个元素的父节点一定是自己右边的节点。
"""


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        # n = len(nums)
        # res = [0] * n
        # sl = SortedList()
        # for i in range(n-1, -1, -1):        # 反向遍历
        #     cnt = sl.bisect_left(nums[i])   # 找到右边比当前值小的元素个数
        #     res[i] = cnt                    # 记入答案
        #     sl.add(nums[i])                 # 将当前值加入有序数组中
        # return res

        # '''根据nums[*][0]进行排序，对应的index随之移动'''
        # def mergeSort(nums, low, high):
        #     if low >= high:     # 递归终止
        #         return 0
        #     '''递归排序'''
        #     mid = low + (high-low)//2
        #     mergeSort(nums, low, mid)           # 左半部分逆序对数目
        #     mergeSort(nums, mid+1, high)        # 右半部分逆序对数目
        #     '''nums[low, mid] 和 nums[mid+1, high] 已排序好'''
        #     tmp = []                            # 记录nums[low, high]排序结果
        #     left, right = low, mid+1
        #     while left<=mid and right<=high:
        #         if nums[left][0] <= nums[right][0]:         # 根据nums[*][0]进行排序
        #             tmp.append(nums[left])
        #             res[nums[left][1]] += right-(mid+1)     # 记录逆序对数目【对应坐标nums[*][1]处】
        #             left += 1
        #         else:
        #             tmp.append(nums[right])
        #             right += 1
        #     '''左或右数组需遍历完（最多只有一个未遍历完）'''
        #     while left<=mid:
        #         tmp.append(nums[left])
        #         res[nums[left][1]] += right -(mid+1)    # 记录逆序对数目【对应坐标nums[*][1]处】
        #         left += 1
        #     while right<=high:
        #         tmp.append(nums[right])
        #         right += 1
        #     nums[low:high+1] = tmp
        # '''主程序'''
        # n = len(nums)
        # res = [0] * n               # 存储结果
        # nums = [(num, idx) for idx, num in enumerate(nums)]
        # # 每个数值附上其对应的索引：
        # # 此时，nums[i][0]表示原来的数值，而nums[i][1]则表示原数值对应的索引（方便定位）
        # mergeSort(nums, 0, n-1)     # 归并排序
        # return res

        class FenwickTree:
            def __init__(self, n):
                self.size = n
                self.tree = [0 for _ in range(n + 1)]

            def __lowbit(self, index):
                return index & (-index)

            # 单点更新：将 index 这个位置 + 1
            def update(self, index, delta):
                # 从下到上，最多到 size，可以等于 size
                while index <= self.size:
                    self.tree[index] += delta
                    index += self.__lowbit(index)

            # 区间查询：查询小于等于 index 的元素个数
            # 查询的语义是"前缀和"
            def query(self, index):
                res = 0
                # 从上到下，最少到 1，可以等于 1
                while index > 0:
                    res += self.tree[index]
                    index -= self.__lowbit(index)
                return res

        # 特判
        size = len(nums)
        if size == 0:
            return []
        if size == 1:
            return [0]
        # 去重，方便离散化
        s = list(set(nums))
        s_len = len(s)
        # 离散化，借助堆
        import heapq
        heapq.heapify(s)
        rank_map = dict()
        rank = 1
        for _ in range(s_len):
            num = heapq.heappop(s)
            rank_map[num] = rank
            rank += 1
        fenwick_tree = FenwickTree(s_len)
        # 从后向前填表
        res = [None for _ in range(size)]
        # 从后向前填表
        for index in range(size - 1, -1, -1):
            # 1、查询排名
            rank = rank_map[nums[index]]
            # 2、在树状数组排名的那个位置 + 1
            fenwick_tree.update(rank, 1)
            # 3、查询一下小于等于“当前排名 - 1”的元素有多少
            res[index] = fenwick_tree.query(rank - 1)
        return res

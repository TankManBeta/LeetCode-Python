# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/4/19 14:24
"""
"""
给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。
你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
返回 滑动窗口中的最大值 。

输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
输出：[3,3,5,5,6,7]
解释：
滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

输入：nums = [1], k = 1
输出：[1]
"""
"""
思路：
（1）暴力超时
（2）大根堆，每次加入的时候看堆顶的index是否在滑动窗口的范围之内，要是在的话就取出，否则一直弹出
（3）双端队列，队头保存当前最大元素的下标，每次来一个新的元素都和队尾比较，如果当前元素比队尾大就把队尾的删除，直到队列为空或者
队尾元素比当前元素大
"""


class Solution(object):
    @staticmethod
    def maxSlidingWindow(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # n = len(nums)
        # ans = []
        # for i in range(k-1, n):
        #     ans.append(max(nums[i-k+1:i+1]))
        # return ans

        # n = len(nums)
        # # 注意 Python 默认的优先队列是小根堆
        # q = [(-nums[i], i) for i in range(k)]
        # heapq.heapify(q)
        # ans = [-q[0][0]]
        # for i in range(k, n):
        #     heapq.heappush(q, (-nums[i], i))
        #     while q[0][1] <= i - k:
        #         heapq.heappop(q)
        #     ans.append(-q[0][0])
        # return ans

        window = []
        res = []
        n = len(nums)
        for i in range(k):
            while window and nums[i] > nums[window[-1]]:
                window.pop()
            window.append(i)
        res.append(nums[window[0]])
        for i in range(k, n):
            if window and window[0] <= i-k:
                window.pop(0)
            while window and nums[i] > nums[window[-1]]:
                window.pop()
            window.append(i)
            res.append(nums[window[0]])
        return res

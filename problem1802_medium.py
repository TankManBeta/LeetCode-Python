# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/1/4 22:07
"""
"""
给你三个正整数 n、index 和 maxSum 。你需要构造一个同时满足下述所有条件的数组 nums（下标 从 0 开始 计数）：
    nums.length == n
    nums[i] 是 正整数 ，其中 0 <= i < n
    abs(nums[i] - nums[i+1]) <= 1 ，其中 0 <= i < n-1
    nums 中所有元素之和不超过 maxSum
    nums[index] 的值被 最大化
返回你所构造的数组中的 nums[index] 。
注意：abs(x) 等于 x 的前提是 x >= 0 ；否则，abs(x) 等于 -x 。

示例 1：
输入：n = 4, index = 2,  maxSum = 6
输出：2
解释：数组 [1,1,2,1] 和 [1,2,2,1] 满足所有条件。不存在其他在指定下标处具有更大值的有效数组。

示例 2：
输入：n = 6, index = 1,  maxSum = 10
输出：3
"""
"""
思路：二分查找，如果我们确定了 nums[index] 的值为 x，此时我们可以找到一个最小的数组总和。也就是说，在 index 左侧的数组元素
从 x−1 每次递减 1，如果减到 1 后还有剩余元素，那么剩余的元素都为 1；同样的，在 index 及右侧的数组元素从 x 也是每次递减 1，
如果减到 1 后还有剩余元素，那么剩余的元素也都为 1。这样我们就可以计算出数组的总和，如果总和小于等于 maxSum，那么此时的 x 
是合法的。随着 x 的增大，数组的总和也会增大，因此我们可以使用二分查找的方法，找到一个最大的且符合条件的 x。为了方便计算数组左侧、
右侧的元素之和，我们定义一个函数 sum(x,cnt)，表示一共有 cnt 个元素，且最大值为 x 的数组的总和。函数 sum(x,cnt) 可以分为两种情况：
如果 x≥cnt，说明最小值减小不到1，那么数组的总和为 (x+x−cnt+1)×cnt/2；如果 x<cnt，说明最小值减小到了1，剩下的全都赋值为1，
那么数组的总和为 (x+1)×x/2+cnt−x。接下来，定义二分的左边界 left=1，右边界 right = maxSum，然后二分查找 nums[index] 的值 mid，
如果 sum(mid - 1, index) + sum(mid, n - index) ≤ maxSum，那么此时的 mid 是合法的，我们可以将 left 更新为 mid，否则我们将 
right 更新为 mid - 1。最后将 left 作为答案返回即可。
"""


class Solution:
    @staticmethod
    def maxValue(n: int, index: int, maxSum: int) -> int:
        def my_sum(x, cnt):
            return (x + x - cnt + 1) * cnt // 2 if x >= cnt else (x + 1) * x // 2 + cnt - x

        left, right = 1, maxSum
        while left < right:
            mid = (left + right + 1) >> 1
            if my_sum(mid - 1, index) + my_sum(mid, n - index) <= maxSum:
                left = mid
            else:
                right = mid - 1
        return left

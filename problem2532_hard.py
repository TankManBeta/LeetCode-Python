# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/7/7 21:24
"""
import heapq
import sys
from typing import List

"""
共有 k 位工人计划将 n 个箱子从旧仓库移动到新仓库。给你两个整数 n 和 k，以及一个二维整数数组 time ，数组的大小为 k x 4 ，
其中 time[i] = [leftToRighti, pickOldi, rightToLefti, putNewi] 。
一条河将两座仓库分隔，只能通过一座桥通行。旧仓库位于河的右岸，新仓库在河的左岸。开始时，所有 k 位工人都在桥的左侧等待。
为了移动这些箱子，第 i 位工人（下标从 0 开始）可以：
    从左岸（新仓库）跨过桥到右岸（旧仓库），用时 leftToRighti 分钟。
    从旧仓库选择一个箱子，并返回到桥边，用时 pickOldi 分钟。不同工人可以同时搬起所选的箱子。
    从右岸（旧仓库）跨过桥到左岸（新仓库），用时 rightToLefti 分钟。
    将箱子放入新仓库，并返回到桥边，用时 putNewi 分钟。不同工人可以同时放下所选的箱子。
如果满足下面任一条件，则认为工人 i 的 效率低于 工人 j ：
    leftToRighti + rightToLefti > leftToRightj + rightToLeftj
    leftToRighti + rightToLefti == leftToRightj + rightToLeftj 且 i > j
工人通过桥时需要遵循以下规则：
    如果工人 x 到达桥边时，工人 y 正在过桥，那么工人 x 需要在桥边等待。
    如果没有正在过桥的工人，那么在桥右边等待的工人可以先过桥。如果同时有多个工人在右边等待，那么 效率最低 的工人会先过桥。
    如果没有正在过桥的工人，且桥右边也没有在等待的工人，同时旧仓库还剩下至少一个箱子需要搬运，此时在桥左边的工人可以过桥。
    如果同时有多个工人在左边等待，那么 效率最低 的工人会先过桥。
    所有 n 个盒子都需要放入新仓库，请你返回最后一个搬运箱子的工人 到达河左岸 的时间。
"""
"""
思路：在本题中，工人共有 4 种状态：在左侧等待；在右侧等待；在左侧工作（放下所选箱子）；在右侧工作（搬起所选箱子）。每一种工作状态
都有相应的优先级计算方法，因此我们用 4 个优先队列来存放处于每种状态下的工人集合：
    在左侧等待的工人：wait_left，题目中定义的效率越高，优先级越高。
    在右侧等待的工人：wait_right，题目中定义的效率越高，优先级越高。
    在左侧工作的工人：work_left，完成时间越早，优先级越高。
    在右侧工作的工人：work_right，完成时间越早，优先级越高。
我们令 remain 表示右侧还有多少个箱子需要搬运，当 remain>0 时，搬运工作需要继续。除此之外，题目求解的是最后一个回到左边的工人的
到达时间，因此当右侧还有工人在等待或在工作时（即 work_right 或 wait_right 不为空），搬运工作就需要继续：
    若 work_left 或 work_right 中的工人在此刻已经完成工作，则需要将它们取出并分别加入到 wait_left 和 wait_right 中。
    若 wait_right 不为空，则取其中优先级最低的工人过桥，将其加入到 work_left 队列中，并将时间更改为过桥后的时间。继续下一轮循环。
    若 remain>0，并且 wait_left 不为空，则需要取优先级最低的工人过桥去取箱子，将其加入到 work_right 队列中，令 remain 减 1，
    并将时间更改为过桥后的时间。继续下一轮循环。
    若 2 和 3 都不满足，表示当前没有人需要过桥，当前时间应该过渡到 work_left 和 work_right 中的最早完成时间。然后继续下一轮循环。
按照上述过程模拟，直到循环条件不再满足。
"""


class Solution:
    @staticmethod
    def findCrossingTime(n: int, k: int, time: List[List[int]]) -> int:
        # 根据时间进行排序，sort默认值相同时，下标大的放后。
        # 根据题目规则，过桥时间相同的下标大的效率低，因此效率低的就会放后。
        # 而过桥时间不同的，时间大的效率低。而前面确定了效率低的放后，说明时间大的要放后，因此对时间进行升序排序
        # 排序后效率低的编号大，根据下标即可确定工人的效率高低
        time.sort(key=lambda t: t[0] + t[2])
        # 初始化
        currTime, remain = 0, n
        waitLefts = [-i for i in range(k - 1, -1, -1)]  # 初始化左岸等待队列，效率低的优先，因此倒序遍历工人编号。由于进行大顶堆排序需要使用负号进行改变排序方向，因此引入负号
        waitRights = []
        workLefts = []
        workRights = []
        # 只要还有剩余箱子或者右岸还有工人，就模拟搬运
        while remain > 0 or waitRights or workRights:
            # 1. 若 workLeft 或 workRight 中的工人完成工作，则将他们取出，并分别放置到 waitLeft 和 waitRight 中。
            while workLefts and workLefts[0][0] <= currTime:
                p = heapq.heappop(workLefts)  # 返回一个左岸完成工作的工人, p = [finishTime, i]
                heapq.heappush(waitLefts, -p[1])  # 将完成工作的工人加入左岸等待队列，且效率低在堆顶。由于效率低的编号大，因此要实现的是大顶堆，编号之前加入负号实现
            while workRights and workRights[0][0] <= currTime:
                p = heapq.heappop(workRights)  # 返回一个右岸完成工作的工人, p = [finishTime, i]
                heapq.heappush(waitRights, -p[1])  # 将完成工作的工人加入右岸等待队列
            if waitRights:
                # 2.若右侧有工人在等待，则取出优先级最低的工人并过桥
                i = -heapq.heappop(waitRights)
                currTime += time[i][2]  # 更新当前时刻，当前时刻 + 右到左的过桥时间
                heapq.heappush(workLefts, [currTime + time[i][3], i])  # 右到左的工人完成时间为到达左岸时刻 + 放下箱子的时间
            elif remain > 0 and waitLefts:
                # 3. 若右侧还有箱子，并且左侧有工人在等待，则取出优先级最低的工人并过桥
                i = -heapq.heappop(waitLefts)
                currTime += time[i][0]  # 更新当前时刻，当前时刻 + 左到右的过桥时间
                heapq.heappush(workRights, [currTime + time[i][1], i])  # 左到右的工人完成时间为到达右岸时刻 + 搬起箱子的时间
                remain -= 1  # 过去一个工人剩余箱子数就减1
            else:
                # 4. 否则，没有人需要过桥，时间过渡到 workLeft 和 workRight 中的最早完成时间
                nextTime = sys.maxsize
                if workLefts:
                    nextTime = min(nextTime, workLefts[0][0])  # 查看workLefts堆顶元素workLefts[0]
                if workRights:
                    nextTime = min(nextTime, workRights[0][0])  # 查看workRights堆顶元素workRights[0]
                if nextTime != sys.maxsize:
                    currTime = max(currTime, nextTime)
        return currTime

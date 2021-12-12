# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2021/12/11 14:23
"""
"""
给你两个整数数组 persons 和 times 。在选举中，第 i 张票是在时刻为 times[i] 时投给候选人 persons[i] 的。
对于发生在时刻 t 的每个查询，需要找出在 t 时刻在选举中领先的候选人的编号。
在 t 时刻投出的选票也将被计入我们的查询之中。在平局的情况下，最近获得投票的候选人将会获胜。
实现 TopVotedCandidate 类：
TopVotedCandidate(int[] persons, int[] times) 使用 persons 和 times 数组初始化对象。
int q(int t) 根据前面描述的规则，返回在时刻 t 在选举中领先的候选人的编号。

输入：
["TopVotedCandidate", "q", "q", "q", "q", "q", "q"]
[[[0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30]], [3], [12], [25], [15], [24], [8]]
输出：
[null, 0, 1, 1, 0, 0, 1]

解释：
TopVotedCandidate topVotedCandidate = new TopVotedCandidate([0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30]);
topVotedCandidate.q(3); // 返回 0 ，在时刻 3 ，票数分布为 [0] ，编号为 0 的候选人领先。
topVotedCandidate.q(12); // 返回 1 ，在时刻 12 ，票数分布为 [0,1,1] ，编号为 1 的候选人领先。
topVotedCandidate.q(25); // 返回 1 ，在时刻 25 ，票数分布为 [0,1,1,0,0,1] ，编号为 1 的候选人领先。（在平局的情况下，1 是最近获得投票的候选人）。
topVotedCandidate.q(15); // 返回 0
topVotedCandidate.q(24); // 返回 0
topVotedCandidate.q(8); // 返回 1
"""
"""
思路：用dp，计算在投票的每一个时刻，比较当前投票人和dp[i-1]是否为同一个人，如果是的话dp[i]也是dp[i-1]，并把总票数+1；
如果不是，比较dp[i-1]和当前投票人的票数，只要当前投票人的票数>=dp[i-1]人的票数，则他是新的候选人（最新投票原则）。
运行时就找第一个比当前t大的，取前面一个即可
"""


class TopVotedCandidate(object):

    def __init__(self, persons, times):
        """
        :type persons: List[int]
        :type times: List[int]
        """
        self.persons = persons
        self.times = times
        self.voters = [-1 for _ in range(0, len(persons))]
        self.votes = [0 for _ in range(0, len(persons))]
        self.counts = {}
        for i in range(0, len(self.times)):
            if i == 0:
                self.counts[persons[i]] = 1
                self.voters[i] = persons[i]
            else:
                if self.voters[i-1] == persons[i]:
                    self.counts[persons[i]] = self.counts.get(persons[i], 0) + 1
                    self.voters[i] = persons[i]
                else:
                    self.counts[persons[i]] = self.counts.get(persons[i], 0) + 1
                    if self.counts[persons[i]] >= self.counts[self.voters[i-1]]:
                        self.voters[i] = self.persons[i]
                    else:
                        self.voters[i] = self.voters[i-1]
        # print(self.voters)

    def q(self, t):
        """
        :type t: int
        :rtype: int
        """
        if t < self.times[0]:
            return None
        if t == self.times[0]:
            return self.voters[0]
        if t >= self.times[-1]:
            return self.voters[-1]
        left = 0
        right = len(self.times)-1
        while left <= right:
            mid = (left + right) // 2
            if t == self.times[mid]:
                return self.voters[mid]
            elif t > self.times[mid]:
                left = mid+1
            else:
                right = mid-1
        return self.voters[right]

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)

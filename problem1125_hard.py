# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/4/8 下午3:10
"""
from math import inf
from typing import List

"""
作为项目经理，你规划了一份需求的技能清单 req_skills，并打算从备选人员名单 people 中选出些人组成一个「必要团队」（ 编号为 i 的
备选人员 people[i] 含有一份该备选人员掌握的技能列表）。
所谓「必要团队」，就是在这个团队中，对于所需求的技能列表 req_skills 中列出的每项技能，团队中至少有一名成员已经掌握。
可以用每个人的编号来表示团队中的成员：
    例如，团队 team = [0, 1, 3] 表示掌握技能分别为 people[0]，people[1]，和 people[3] 的备选人员。
请你返回 任一 规模最小的必要团队，团队成员用人员编号表示。你可以按 任意顺序 返回答案，题目数据保证答案存在。

示例 1：
输入：req_skills = ["java","nodejs","reactjs"], people = [["java"],["nodejs"],["nodejs","reactjs"]]
输出：[0,2]

示例 2：
输入：req_skills = ["algorithms","math","java","reactjs","csharp","aws"], people = [["algorithms","math","java"],
["algorithms","math","reactjs"],["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]]
输出：[1,2]
"""
"""
思路：首先将res_skills中的每一个技能编号。然后，我们遍历 people 中的每个人，将其掌握的技能用二进制数表示，即 p[i] 表示编号为 
i 的人掌握的技能。
接下来，我们定义以下三个数组，其中：
    数组 f[i] 表示掌握技能集合为 i 的最少人数，其中 i 的二进制表示中的每一位为 1 的位置，表示对应的技能被掌握。初始时 f[0]=0，
    其余位置均为无穷大。
    数组 g[i] 表示掌握技能集合为 i 的最少人数时，最后一个人的编号。
    数组 h[i] 表示掌握技能集合为 i 的最少人数时，上一个技能集合状态。
我们在 [0,...,2**m−1] 的范围内枚举每个技能集合，对于每个技能集合 i：
我们枚举 people 中的每个人 j，如果 f[i]+1<f[i∣p[j]]，说明 f[i∣p[j]] 可以通过 f[i] 转移得到，此时，我们更新 f[i∣p[j]] 为 f[i]+1，
并将 g[i∣p[j]] 更新为 j，同时将 h[i∣p[j]] 更新为 i。即当前技能集合状态为 i∣p[j] 时，最后一个人的编号为 j，上一个技能集合状态为 i。
最后，我们从技能集合 i=2**m−1 开始，找到此时最后一个人的编号 g[i]，将其加入答案中，然后将 i 更新为 h[i]，不断地向前回溯，直到 
i=0，即可得到最小的必要团队中的人员编号。
"""


class Solution:
    @staticmethod
    def smallestSufficientTeam(req_skills: List[str], people: List[List[str]]) -> List[int]:
        # req_skills = sorted(req_skills)
        # n = len(people)
        # ans = [i for i in range(n)]
        # for i in range(1<<n):
        #     tmp_ans = []
        #     tmp_skills = set()
        #     for j in range(n):
        #         if (1<<j) & i:
        #             tmp_ans.append(j)
        #             for skill in people[j]:
        #                 tmp_skills.add(skill)
        #     if sorted(list(tmp_skills)) == req_skills and len(ans) > len(tmp_ans):
        #         ans = tmp_ans
        # return ans

        # 给技能编号
        d = {s: i for i, s in enumerate(req_skills)}
        m, n = len(req_skills), len(people)
        # 每个人掌握的技能
        p = [0] * n
        for i, skills in enumerate(people):
            for skill in skills:
                p[i] |= 1 << d[skill]
        # 掌握技能集合i的最少人数
        f = [inf] * (1 << m)
        # 掌握技能集合i时，最后一人的编号
        g = [0] * (1 << m)
        # 掌握技能集合i时，上一个的技能集合
        h = [0] * (1 << m)
        f[0] = 0
        for i in range(1 << m):
            if f[i] == inf:
                continue
            for j in range(n):
                if f[i] + 1 < f[i | p[j]]:
                    f[i | p[j]] = f[i] + 1
                    g[i | p[j]] = j
                    h[i | p[j]] = i
        i = (1 << m) - 1
        ans = []
        while i:
            ans.append(g[i])
            i = h[i]
        return ans

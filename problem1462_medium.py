# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/9/12 21:59
"""
from typing import List

"""
你总共需要上 numCourses 门课，课程编号依次为 0 到 numCourses-1 。你会得到一个数组 prerequisite ，其中 prerequisites[i] = [ai, bi] 
表示如果你想选 bi 课程，你 必须 先选 ai 课程。
有的课会有直接的先修课程，比如如果想上课程 1 ，你必须先上课程 0 ，那么会以 [0,1] 数对的形式给出先修课程数对。
先决条件也可以是 间接 的。如果课程 a 是课程 b 的先决条件，课程 b 是课程 c 的先决条件，那么课程 a 就是课程 c 的先决条件。
你也得到一个数组 queries ，其中 queries[j] = [uj, vj]。对于第 j 个查询，您应该回答课程 uj 是否是课程 vj 的先决条件。
返回一个布尔数组 answer ，其中 answer[j] 是第 j 个查询的答案。 

示例 1：
输入：numCourses = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]]
输出：[false,true]
解释：课程 0 不是课程 1 的先修课程，但课程 1 是课程 0 的先修课程。

示例 2：
输入：numCourses = 2, prerequisites = [], queries = [[1,0],[0,1]]
输出：[false,false]
解释：没有先修课程对，所以每门课程之间是独立的。

示例 3：
输入：numCourses = 3, prerequisites = [[1,2],[1,0],[2,0]], queries = [[1,0],[1,2]]
输出：[true,true]
"""
"""
思路：我们创建一个二维数组 f，其中 f[i][j] 表示节点 i 到节点 j 是否可达。接下来，我们遍历先修课程数组 prerequisites，对于其中的每一项 
[a,b]，我们将 f[a][b] 设为 true。然后，我们使用 Floyd 算法计算出所有节点对之间的可达性。具体地，我们使用三重循环，首先枚举中间点 k，
接下来枚举起点 i，最后枚举终点 j。对于每一次循环，如果节点 i 到节点 k 可达，且节点 k 到节点 j 可达，那么节点 i 到节点 j 也是可达的，我们将 
f[i][j] 设为 true。在计算完所有节点对之间的可达性之后，对于每一个查询 [a,b]，我们直接返回 f[a][b] 即可。
"""


class Solution:
    @staticmethod
    def checkIfPrerequisite(
            n: int, prerequisites: List[List[int]], queries: List[List[int]]
    ) -> List[bool]:
        f = [[False] * n for _ in range(n)]
        for a, b in prerequisites:
            f[a][b] = True
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if f[i][k] and f[k][j]:
                        f[i][j] = True
        return [f[a][b] for a, b in queries]

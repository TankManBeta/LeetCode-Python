# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/1/20 19:49
"""
from collections import deque
from typing import List

"""
病毒扩散得很快，现在你的任务是尽可能地通过安装防火墙来隔离病毒。
假设世界由 m x n 的二维矩阵 isInfected 组成， isInfected[i][j] == 0 表示该区域未感染病毒，而  isInfected[i][j] == 1 表示
该区域已感染病毒。可以在任意 2 个相邻单元之间的共享边界上安装一个防火墙（并且只有一个防火墙）。
每天晚上，病毒会从被感染区域向相邻未感染区域扩散，除非被防火墙隔离。现由于资源有限，每天你只能安装一系列防火墙来隔离其中一个
被病毒感染的区域（一个区域或连续的一片区域），且该感染区域对未感染区域的威胁最大且 保证唯一 。
你需要努力使得最后有部分区域不被病毒感染，如果可以成功，那么返回需要使用的防火墙个数; 如果无法实现，则返回在世界被病毒全部感染时
已安装的防火墙个数。

示例 1：
输入: isInfected = [[0,1,0,0,0,0,0,1],[0,1,0,0,0,0,0,1],[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0]]
输出: 10
解释:一共有两块被病毒感染的区域。
在第一天，添加 5 墙隔离病毒区域的左侧。病毒传播后的状态是:
第二天，在右侧添加 5 个墙来隔离病毒区域。此时病毒已经被完全控制住了。

示例 2：
输入: isInfected = [[1,1,1],[1,0,1],[1,1,1]]
输出: 4
解释: 虽然只保存了一个小区域，但却有四面墙。
注意，防火墙只建立在两个不同区域的共享边界上。

示例 3:
输入: isInfected = [[1,1,1,0,0,0,0,0,0],[1,0,1,0,1,1,1,1,1],[1,1,1,0,0,0,0,0,0]]
输出: 13
解释: 在隔离右边感染区域后，隔离左边病毒区域只需要 2 个防火墙。
"""
"""
思路：我们首先可以对矩阵 isInfected 进行广度优先搜索，具体地，当我们遍历到 isInfected 中的一个 1 时，就从这个 1 对应的位置开始
进行广度优先搜索，这样就可以得到连续的一块被病毒感染的区域。在搜索的过程中，如果当前是第 idx (idx≥1) 块被病毒感染的区域，我们就
把这些 1 都赋值成 −idx，这样就可以防止重复搜索，并且可以和非病毒区域 0 区分开来。同时，由于我们每次需要选择「对未感染区域的威胁
最大」的区域设置防火墙，因此我们还需要存储：
    该区域相邻的未感染区域（即 0）的位置和个数；
    如果需要位该区域设置防火墙，那么需要防火墙的个数。
对于前者，我们在广度优先搜索的过程中，只要在扩展 1 时搜索相邻的 0，就可以把这个 0 对应的位置放在一个哈希集合中。这里使用哈希集合
的原因是同一个 0 可能会和多个 1 相邻，可以防止重复计算。同时，由于多个 1 可能出现在不同的感染区域中，如果通过修改矩阵 isInfected 
的形式来标记这些 0，会使得代码编写较为麻烦。
对于后者，计算的方法是类似的，在扩展 1 时如果搜索到相邻的 0，那么我们就需要在 1 和 0 之间的这条网格边上建一个防火墙。同一个 0 和
多个 1 相邻，就需要建立多个防火墙，因此我们只需要使用一个变量在广度优先搜索的过程中计数即可，无需考虑重复的情况。
在广度优先搜索完成后，如果我们没有发现任何感染区域，说明区域内不存在病毒，我们直接返回 0 作为答案。否则，我们需要找到「对未感染
区域的威胁最大」的区域，这里只需要找出对应的哈希集合的大小最大的那块区域即可。
在确定了区域（假设是第 idx 块区域）后，我们把矩阵中所有的 −idx 都变成 2，这样可以不影响任何搜索和判断；除此之外的所有负数都恢复
成 1。此外，所有哈希集合中存储的（除了第 idx 块区域对应的以外）所有相邻位置都需要从 0 变成 1，表示病毒的传播。
最后，如果我们发现区域一共只有一块，那么这次防火墙建立后，不会再有病毒传播，可以返回答案；否则我们还需要继续重复执行上述的所有步骤。
"""


class Solution:
    @staticmethod
    def containVirus(isInfected: List[List[int]]) -> int:
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        m, n = len(isInfected), len(isInfected[0])
        ans = 0

        while True:
            neighbors, firewalls = list(), list()
            for i in range(m):
                for j in range(n):
                    if isInfected[i][j] == 1:
                        # 第1块就把当前连通块的全都置为-1，第2块就全都置为-2，以此类推
                        q = deque([(i, j)])
                        neighbor = set()
                        firewall, idx = 0, len(neighbors) + 1
                        isInfected[i][j] = -idx

                        while q:
                            x, y = q.popleft()
                            for d in range(4):
                                nx, ny = x + dirs[d][0], y + dirs[d][1]
                                if 0 <= nx < m and 0 <= ny < n:
                                    # 找到最大的联通块
                                    if isInfected[nx][ny] == 1:
                                        q.append((nx, ny))
                                        isInfected[nx][ny] = -idx
                                    # 周围未被感染的邻居加防火墙
                                    elif isInfected[nx][ny] == 0:
                                        firewall += 1
                                        neighbor.add((nx, ny))

                        neighbors.append(neighbor)
                        firewalls.append(firewall)

            if not neighbors:
                break

            # 找到感染区域最大的块
            idx = 0
            for i in range(1, len(neighbors)):
                if len(neighbors[i]) > len(neighbors[idx]):
                    idx = i

            # 将其他块还原，被感染的块就置为2
            ans += firewalls[idx]
            for i in range(m):
                for j in range(n):
                    if isInfected[i][j] < 0:
                        if isInfected[i][j] != -idx - 1:
                            isInfected[i][j] = 1
                        else:
                            isInfected[i][j] = 2

            # 对于没有被拦截的要扩散
            for i, neighbor in enumerate(neighbors):
                if i != idx:
                    for x, y in neighbor:
                        isInfected[x][y] = 1

            if len(neighbors) == 1:
                break

        return ans

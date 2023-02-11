# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/2/8 0:25
"""
from typing import List

"""
你是一位系统管理员，手里有一份文件夹列表 folder，你的任务是要删除该列表中的所有 子文件夹，并以 任意顺序 返回剩下的文件夹。
如果文件夹 folder[i] 位于另一个文件夹 folder[j] 下，那么 folder[i] 就是 folder[j] 的 子文件夹 。
文件夹的「路径」是由一个或多个按以下格式串联形成的字符串：'/' 后跟一个或者多个小写英文字母。
例如，"/leetcode" 和 "/leetcode/problems" 都是有效的路径，而空字符串和 "/" 不是。

示例 1：
输入：folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
输出：["/a","/c/d","/c/f"]
解释："/a/b/" 是 "/a" 的子文件夹，而 "/c/d/e" 是 "/c/d" 的子文件夹。

示例 2：
输入：folder = ["/a","/a/b/c","/a/b/d"]
输出：["/a"]
解释：文件夹 "/a/b/c" 和 "/a/b/d/" 都会被删除，因为它们都是 "/a" 的子文件夹。

示例 3：
输入: folder = ["/a/b/c","/a/b/ca","/a/b/d"]
输出: ["/a/b/c","/a/b/ca","/a/b/d"]
"""
"""
思路：先排序再挨个扫描。如果当前的路径f不是以我们想要的t开头，说明他不是子路径，就把我们的t更新为f+'/'继续扫描。
"""


class Solution:
    @staticmethod
    def removeSubfolders(folder: List[str]) -> List[str]:
        res, t = [], ' '
        for f in sorted(folder):
            if not f.startswith(t):
                res.append(f)
                t = f + '/'
        return res
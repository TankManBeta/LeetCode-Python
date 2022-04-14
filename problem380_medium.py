# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/4/13 13:36
"""
from random import choice

"""
实现RandomizedSet 类：
    RandomizedSet() 初始化 RandomizedSet 对象
    bool insert(int val) 当元素 val 不存在时，向集合中插入该项，并返回 true ；否则，返回 false 。
    bool remove(int val) 当元素 val 存在时，从集合中移除该项，并返回 true ；否则，返回 false 。
    int getRandom()随机返回现有集合中的一项（测试用例保证调用此方法时集合中至少存在一个元素）。每个元素应该有相同的概率被返回。
你必须实现类的所有函数，并满足每个函数的 平均 时间复杂度为 O(1) 。

输入
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
输出
[null, true, false, true, 2, true, false, 2]

解释
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // 向集合中插入 1 。返回 true 表示 1 被成功地插入。
randomizedSet.remove(2); // 返回 false ，表示集合中不存在 2 。
randomizedSet.insert(2); // 向集合中插入 2 。返回 true 。集合现在包含 [1,2] 。
randomizedSet.getRandom(); // getRandom 应随机返回 1 或 2 。
randomizedSet.remove(1); // 从集合中移除 1 ，返回 true 。集合现在包含 [2] 。
randomizedSet.insert(2); // 2 已在集合中，所以返回 false 。
randomizedSet.getRandom(); // 由于 2 是集合中唯一的数字，getRandom 总是返回 2 。
"""
"""
思路：数组可以O(1)时间查找，但不能O(1)时间插入删除，哈希表相反，所以考虑两个结合，哈希表存储当前值和当前值所在的位置，然后删除
时直接把数组最后一个换到当前要删除的元素的地方即可
"""


class RandomizedSet(object):

    def __init__(self):
        self.nums_list = []
        self.nums_dict = {}

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.nums_dict:
            return False
        self.nums_dict[val] = len(self.nums_list)
        self.nums_list.append(val)
        return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.nums_dict:
            return False
        val_index = self.nums_dict[val]
        self.nums_list[val_index] = self.nums_list[-1]
        self.nums_dict[self.nums_list[val_index]] = val_index
        self.nums_list.pop()
        del self.nums_dict[val]
        return True

    def getRandom(self):
        """
        :rtype: int
        """
        return choice(self.nums_list)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
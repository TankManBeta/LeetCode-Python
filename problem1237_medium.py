# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/2/19 13:55
"""
from typing import List

"""
给你一个函数  f(x, y) 和一个目标结果 z，函数公式未知，请你计算方程 f(x,y) == z 所有可能的正整数 数对 x 和 y。满足条件的结果数对可以按任意顺序返回。
尽管函数的具体式子未知，但它是单调递增函数，也就是说：
    f(x, y) < f(x + 1, y)
    f(x, y) < f(x, y + 1)
函数接口定义如下：
interface CustomFunction {
public:
  // Returns some positive integer f(x, y) for two positive integers x and y based on a formula.
  int f(int x, int y);
};
你的解决方案将按如下规则进行评判：
    判题程序有一个由 CustomFunction 的 9 种实现组成的列表，以及一种为特定的 z 生成所有有效数对的答案的方法。
    判题程序接受两个输入：function_id（决定使用哪种实现测试你的代码）以及目标结果 z 。
    判题程序将会调用你实现的 findSolution 并将你的结果与答案进行比较。
    如果你的结果与答案相符，那么解决方案将被视作正确答案，即 Accepted 。

示例 1：
输入：function_id = 1, z = 5
输出：[[1,4],[2,3],[3,2],[4,1]]
解释：function_id = 1 暗含的函数式子为 f(x, y) = x + y
以下 x 和 y 满足 f(x, y) 等于 5：
x=1, y=4 -> f(1, 4) = 1 + 4 = 5
x=2, y=3 -> f(2, 3) = 2 + 3 = 5
x=3, y=2 -> f(3, 2) = 3 + 2 = 5
x=4, y=1 -> f(4, 1) = 4 + 1 = 5

示例 2：
输入：function_id = 2, z = 5
输出：[[1,5],[5,1]]
解释：function_id = 2 暗含的函数式子为 f(x, y) = x * y
以下 x 和 y 满足 f(x, y) 等于 5：
x=1, y=5 -> f(1, 5) = 1 * 5 = 5
x=5, y=1 -> f(5, 1) = 5 * 1 = 5
"""
"""
思路：
（1）枚举，根据题目给出的 x 和 y 的取值范围，枚举所有的 x,y 数对，保存满足 f(x,y)=z 的数对，最后返回结果。
（2）二分查找，对于每个x，查找是否有y使得f(x, y) == z
（3）双指针，我们可以定义两个指针 x 和 y，初始时 x=1，y=1000。如果 f(x,y)=z，我们将 (x,y) 加入答案中，然后 x←x+1，y←y−1；
如果 f(x,y)<z，此时对任意的 y′<y，都有 f(x,y′)<f(x,y)<z，因此我们不能将 y 减小，只能将 x 增大，所以 x←x+1；
如果 f(x,y)>z，此时对任意的 x′>x，都有 f(x′,y)>f(x,y)>z，因此我们不能将 x 增大，只能将 y 减小，所以 y←y−1。
"""


"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
"""


class Solution:
    @staticmethod
    def findSolution(customfunction: "CustomFunction", z: int) -> List[List[int]]:
        # ans = []
        # for x in range(1, 1001):
        #     for y in range(1, 1001):
        #         if customfunction.f(x, y) == z:
        #             ans.append([x, y])
        # return ans

        # ans = []
        # for x in range(1, 1001):
        #     y = 1 + bisect_left(range(1, 1000), z, key=lambda y: customfunction.f(x, y))
        #     if customfunction.f(x, y) == z:
        #         ans.append([x, y])
        # return ans

        ans = []
        x, y = 1, 1000
        while x <= 1000 and y:
            t = customfunction.f(x, y)
            if t < z:
                x += 1
            elif t > z:
                y -= 1
            else:
                ans.append([x, y])
                x, y = x + 1, y - 1
        return ans

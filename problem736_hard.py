# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/1/19 21:29
"""
from collections import defaultdict

"""
给你一个类似 Lisp 语句的字符串表达式 expression，求出其计算结果。
表达式语法如下所示:
    表达式可以为整数，let 表达式，add 表达式，mult 表达式，或赋值的变量。表达式的结果总是一个整数。
    (整数可以是正整数、负整数、0)
    let 表达式采用 "(let v1 e1 v2 e2 ... vn en expr)" 的形式，其中 let 总是以字符串 "let"来表示，接下来会跟随一对或多对交替的
    变量和表达式，也就是说，第一个变量 v1被分配为表达式 e1 的值，第二个变量 v2 被分配为表达式 e2 的值，依次类推；最终 let 表达式
    的值为 expr表达式的值。
    add 表达式表示为 "(add e1 e2)" ，其中 add 总是以字符串 "add" 来表示，该表达式总是包含两个表达式 e1、e2 ，最终结果是 e1 
    表达式的值与 e2 表达式的值之 和 。
    mult 表达式表示为 "(mult e1 e2)" ，其中 mult 总是以字符串 "mult" 表示，该表达式总是包含两个表达式 e1、e2，最终结果是 e1 
    表达式的值与 e2 表达式的值之 积 。
    在该题目中，变量名以小写字符开始，之后跟随 0 个或多个小写字符或数字。为了方便，"add" ，"let" ，"mult" 会被定义为 "关键字"，
    不会用作变量名。
    最后，要说一下作用域的概念。计算变量名所对应的表达式时，在计算上下文中，首先检查最内层作用域（按括号计），然后按顺序依次检查
    外部作用域。测试用例中每一个表达式都是合法的。有关作用域的更多详细信息，请参阅示例。
 
示例 1：
输入：expression = "(let x 2 (mult x (let x 3 y 4 (add x y))))"
输出：14
解释：
计算表达式 (add x y), 在检查变量 x 值时，
在变量的上下文中由最内层作用域依次向外检查。
首先找到 x = 3, 所以此处的 x 值是 3 。

示例 2：
输入：expression = "(let x 3 x 2 x)"
输出：2
解释：let 语句中的赋值运算按顺序处理即可。

示例 3：
输入：expression = "(let x 1 y 2 x (add x y) (add x y))"
输出：5
解释：
第一个 (add x y) 计算结果是 3，并且将此值赋给了 x 。 
第二个 (add x y) 计算结果是 3 + 2 = 5 。
"""
"""
思路：定义函数 parseVar 用来解析变量以及函数 parseInt 用来解析整数。使用 scope 来记录作用域，每个变量都依次记录下它从外到内的
所有值，查找时只需要查找最后一个数值。我们递归地解析表达式 expression。
expression 的下一个字符不等于左括号 '('：
    expression 的下一个字符是小写字母，那么表达式是一个变量，使用函数 parseVar 解析变量，然后在 scope 中查找变量的最后一个数值
    即最内层作用域的值并返回结果。
    expression 的下一个字符不是小写字母，那么表达式是一个整数，使用函数 parseInt 解析并返回结果。
去掉左括号后，expression 的下一个字符是 'l'，那么表达式是 let 表达式。对于 let 表达式，需要判断是否已经解析到最后一个 expr 表达式。
    如果下一个字符不是小写字母，或者解析变量后下一个字符是右括号 'l'，说明是最后一个 expr 表达式，计算它的值并返回结果。并且我们
    需要在 scope 中清除 let 表达式对应的作用域变量。
    否则说明是交替的变量 vi 和表达式 ei，在 scope 将变量 vi 的数值列表增加表达式 ei 的数值。
去掉左括号后，expression 的下一个字符是 'a'，那么表达式是 add 表达式。计算 add 表达式对应的两个表达式 e1 和 e2 的值，返回两者之和。
去掉左括号后，expression 的下一个字符是 'm'，那么表达式是 mult 表达式。计算 mult 表达式对应的两个表达式 e1 和 e2 的值，返回两者之积。
"""


class Solution:
    @staticmethod
    def evaluate(expression: str) -> int:
        i, n = 0, len(expression)

        def parseVar() -> str:
            nonlocal i
            i0 = i
            while i < n and expression[i] != ' ' and expression[i] != ')':
                i += 1
            return expression[i0:i]

        def parseInt() -> int:
            nonlocal i
            sign, x = 1, 0
            if expression[i] == '-':
                sign = -1
                i += 1
            while i < n and expression[i].isdigit():
                x = x * 10 + int(expression[i])
                i += 1
            return sign * x

        scope = defaultdict(list)

        def innerEvaluate() -> int:
            nonlocal i
            if expression[i] != '(':  # 非表达式，可能为：整数或变量
                if expression[i].islower():  # 变量
                    return scope[parseVar()][-1]
                return parseInt()  # 整数
            i += 1  # 移除左括号
            if expression[i] == 'l':  # "let" 表达式
                i += 4  # 移除 "let "
                variables = []
                while True:
                    if not expression[i].islower():
                        ret = innerEvaluate()  # let 表达式的最后一个 expr 表达式的值
                        break
                    var = parseVar()
                    if expression[i] == ')':
                        ret = scope[var][-1]  # let 表达式的最后一个 expr 表达式的值
                        break
                    variables.append(var)
                    i += 1  # 移除空格
                    scope[var].append(innerEvaluate())
                    i += 1  # 移除空格
                for var in variables:
                    scope[var].pop()  # 清除当前作用域的变量
            elif expression[i] == 'a':  # "add" 表达式
                i += 4  # 移除 "add "
                e1 = innerEvaluate()
                i += 1  # 移除空格
                e2 = innerEvaluate()
                ret = e1 + e2
            else:  # "mult" 表达式
                i += 5  # 移除 "mult "
                e1 = innerEvaluate()
                i += 1  # 移除空格
                e2 = innerEvaluate()
                ret = e1 * e2
            i += 1  # 移除右括号
            return ret

        return innerEvaluate()

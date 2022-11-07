# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/11/5 14:29
"""
"""
给你一个以字符串形式表述的 布尔表达式（boolean） expression，返回该式的运算结果。
有效的表达式需遵循以下约定：
    "t"，运算结果为 True
    "f"，运算结果为 False
    "!(expr)"，运算过程为对内部表达式 expr 进行逻辑 非的运算（NOT）
    "&(expr1,expr2,...)"，运算过程为对 2 个或以上内部表达式 expr1, expr2, ... 进行逻辑 与的运算（AND）
    "|(expr1,expr2,...)"，运算过程为对 2 个或以上内部表达式 expr1, expr2, ... 进行逻辑 或的运算（OR）
 
示例 1：
输入：expression = "!(f)"
输出：true

示例 2：
输入：expression = "|(f,t)"
输出：true

示例 3：
输入：expression = "&(t,f)"
输出：false

示例 4：
输入：expression = "|(&(t,f,t),!(t))"
输出：false
"""
"""
思路：使用双栈，values用于存放值，operators用于存放操作符，如果遇到','就跳过，如果遇到'('就放到values中，如果遇到')'就从values
中一直弹出，直到values中的值为'('，如果遇到"!|&"中的一个时就加到operators中，遇到't'或'f'就把True或False放入values中。
"""


class Solution:
    @staticmethod
    def parseBoolExpr(expression: str) -> bool:
        operators, values = [], []
        for char in expression:
            if char in ['!', '|', '&']:
                operators.append(char)
            elif char == 't':
                values.append(True)
            elif char == 'f':
                values.append(False)
            elif char == ',':
                continue
            elif char == '(':
                values.append('(')
            else:
                operator = operators.pop()
                targets = []
                while values[-1] != '(':
                    value = values.pop()
                    targets.append(value)
                values.pop()
                if operator == '!':
                    values.append(not targets[0])
                elif operator == '|':
                    values.append(any(targets))
                else:
                    values.append(all(targets))
        return values[-1]

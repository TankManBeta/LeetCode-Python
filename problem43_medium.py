# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2021/12/11 11:55
"""
"""
给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

输入: num1 = "2", num2 = "3"
输出: "6"

输入: num1 = "123", num2 = "456"
输出: "56088"
"""
"""
思路：先从后往前乘，再加，注意进位
"""


class Solution(object):
    @staticmethod
    def multiply(num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == "0" or num2 == "0":
            return "0"
        len_num1 = len(num1)
        len_num2 = len(num2)
        res_list = []
        index_num1 = len_num1 - 1
        index_num2 = len_num2 - 1
        while index_num2 >= 0:
            res_str = ""
            up = 0
            for j in range(index_num1, -1, -1):
                int_num1 = int(num1[j])
                int_num2 = int(num2[index_num2])
                temp = (int_num1 * int_num2 + up) % 10
                up = (int_num1 * int_num2 + up) // 10
                res_str = str(temp) + res_str
            if up > 0:
                res_str = str(up) + res_str
            res_str += "0" * (len_num2 - 1 - index_num2)
            res_list.append(res_str)
            index_num2 -= 1
        # print(res_list)
        final_ans = ""

        for i in range(0, len(res_list)):
            final_ans = "0" * (max(len(res_list[i]), len(final_ans)) - len(final_ans)) + final_ans
            ans_str = ""
            new_up = 0
            for j in range(len(res_list[i]) - 1, -1, -1):
                new_int_num1 = int(final_ans[j])
                new_int_num2 = int(res_list[i][j])
                temp = (new_int_num1 + new_int_num2 + new_up) % 10
                new_up = (new_int_num1 + new_int_num2 + new_up) // 10
                ans_str = str(temp) + ans_str
            if new_up > 0:
                ans_str = str(new_up) + ans_str
            final_ans = ans_str
        return final_ans

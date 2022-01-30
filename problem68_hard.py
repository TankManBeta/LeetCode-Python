# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/1/29 17:42
"""
"""
给定一个单词数组和一个长度 maxWidth，重新排版单词，使其成为每行恰好有 maxWidth 个字符，且左右两端对齐的文本。
你应该使用“贪心算法”来放置给定的单词；也就是说，尽可能多地往每行中放置单词。必要时可用空格 ' ' 填充，使得每行恰好有 maxWidth 个字符。
要求尽可能均匀分配单词间的空格数量。如果某一行单词间的空格不能均匀分配，则左侧放置的空格数要多于右侧的空格数。
文本的最后一行应为左对齐，且单词之间不插入额外的空格。
说明:
单词是指由非空格字符组成的字符序列。
每个单词的长度大于 0，小于等于 maxWidth。
输入单词数组 words 至少包含一个单词。

输入:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
输出:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]

输入:
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
输出:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
解释: 注意最后一行的格式应为 "shall be    " 而不是 "shall     be",
     因为最后一行应为左对齐，而不是左右两端对齐。       
     第二行同样为左对齐，这是因为这行只包含一个单词。

输入:
words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
输出:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
"""
"""
思路：首先判断一行算上空格能放多少单词。然后对分组之后的每一个item进行字符串的组装。如果是最后一行，连接字符串，剩下的添空格；
如果一行只有一个单词，直接后面添空格；剩余情况，首先计算每两个单词之间的空格数，如果能整除，直接平均分配，如果不能整除，
就在前几个空格平均分配多出来的。
"""


class Solution(object):
    @staticmethod
    def full_justify(words, max_width):
        """
        :type words: List[str]
        :type max_width: int
        :rtype: List[str]
        """
        groups = []
        i = 0
        while i < len(words):
            temp_list = []
            temp_count = 0
            while i < len(words) and temp_count + len(words[i]) + len(temp_list) <= max_width:
                temp_list.append(words[i])
                temp_count += len(words[i])
                i += 1
            groups.append(temp_list)

        res = []
        for i in range(len(groups)):
            # last row
            if i == len(groups) - 1:
                temp_str = " ".join(groups[i])
                temp_str += " " * (max_width - len(temp_str))
                # res.append(temp_str)
            else:
                # one word
                if len(groups[i]) == 1:
                    temp_str = groups[i][0] + " " * (max_width - len(groups[i][0]))
                else:
                    temp_count = 0
                    for word in groups[i]:
                        temp_count += len(word)
                    # amount of total blanks
                    blank_count = max_width - temp_count
                    # amount of blanks in each interval
                    interval = int(blank_count / (len(groups[i]) - 1))
                    # whether there is remainder
                    remainder = blank_count % (len(groups[i]) - 1)
                    # deal with first word so that the others can be handled more easily
                    temp_str = groups[i][0]
                    if remainder == 0:
                        for word in groups[i][1:]:
                            temp_str = temp_str + " " * interval + word
                    else:
                        for j in range(1, len(groups[i])):
                            if j <= remainder:
                                temp_str = temp_str + " " * (interval + 1) + groups[i][j]
                            else:
                                temp_str = temp_str + " " * interval + groups[i][j]
            res.append(temp_str)
        return res

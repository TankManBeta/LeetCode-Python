# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2021/12/4 16:59
"""
s = "barfoothefoobarman"
words = ["foo", "bar"]
len_words = len(words)
len_word = len(words[0])
len_window = len(words) * len(words[0])
len_s = len(s)
start = 0
end = len_window - 1
option_list = [s[start + len_word * i: start + len_word * (i + 1)] for i in range(0, len_words)]
print(option_list)

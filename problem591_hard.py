# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/1/16 21:27
"""
"""
给定一个表示代码片段的字符串，你需要实现一个验证器来解析这段代码，并返回它是否合法。合法的代码片段需要遵守以下的所有规则：
    代码必须被合法的闭合标签包围。否则，代码是无效的。
    闭合标签（不一定合法）要严格符合格式：<TAG_NAME>TAG_CONTENT</TAG_NAME>。其中，<TAG_NAME>是起始标签，</TAG_NAME>是结束标签。
    起始和结束标签中的 TAG_NAME 应当相同。当且仅当 TAG_NAME 和 TAG_CONTENT 都是合法的，闭合标签才是合法的。
    合法的 TAG_NAME 仅含有大写字母，长度在范围 [1,9] 之间。否则，该 TAG_NAME 是不合法的。
    合法的 TAG_CONTENT 可以包含其他合法的闭合标签，cdata （请参考规则7）和任意字符（注意参考规则1）除了不匹配的<、不匹配的起始
    和结束标签、不匹配的或带有不合法 TAG_NAME 的闭合标签。否则，TAG_CONTENT 是不合法的。
    一个起始标签，如果没有具有相同 TAG_NAME 的结束标签与之匹配，是不合法的。反之亦然。不过，你也需要考虑标签嵌套的问题。
    一个<，如果你找不到一个后续的>与之匹配，是不合法的。并且当你找到一个<或</时，所有直到下一个>的前的字符，都应当被解析为 
    TAG_NAME（不一定合法）。
    cdata 有如下格式：<![CDATA[CDATA_CONTENT]]>。CDATA_CONTENT 的范围被定义成 <![CDATA[ 和后续的第一个 ]]>之间的字符。
    CDATA_CONTENT 可以包含任意字符。cdata 的功能是阻止验证器解析CDATA_CONTENT，所以即使其中有一些字符可以被解析为标签
    （无论合法还是不合法），也应该将它们视为常规字符。
合法代码的例子:
输入: "<DIV>This is the first line <![CDATA[<div>]]></DIV>"
输出: True
解释: 
代码被包含在了闭合的标签内： <DIV> 和 </DIV> 。
TAG_NAME 是合法的，TAG_CONTENT 包含了一些字符和 cdata 。 
即使 CDATA_CONTENT 含有不匹配的起始标签和不合法的 TAG_NAME，它应该被视为普通的文本，而不是标签。
所以 TAG_CONTENT 是合法的，因此代码是合法的。最终返回True。

输入: "<DIV>>>  ![cdata[]] <![CDATA[<div>]>]]>]]>>]</DIV>"
输出: True
解释:
我们首先将代码分割为： start_tag|tag_content|end_tag 。
start_tag -> "<DIV>"
end_tag -> "</DIV>"
tag_content 也可被分割为： text1|cdata|text2 。
text1 -> ">>  ![cdata[]] "
cdata -> "<![CDATA[<div>]>]]>" ，其中 CDATA_CONTENT 为 "<div>]>"
text2 -> "]]>>]"
start_tag 不是 "<DIV>>>" 的原因参照规则 6 。
cdata 不是 "<![CDATA[<div>]>]]>]]>" 的原因参照规则 7 。

不合法代码的例子:
输入: "<A>  <B> </A>   </B>"
输出: False
解释: 不合法。如果 "<A>" 是闭合的，那么 "<B>" 一定是不匹配的，反之亦然。

输入: "<DIV>  div tag is not closed  <DIV>"
输出: False

输入: "<DIV>  unmatched <  </DIV>"
输出: False

输入: "<DIV> closed tags with invalid tag name  <b>123</b> </DIV>"
输出: False

输入: "<DIV> unmatched tags with invalid tag name  </1234567890> and <CDATA[[]]>  </DIV>"
输出: False

输入: "<DIV>  unmatched start tag <B>  and unmatched end tag </C>  </DIV>"
输出: False
"""
"""
思路：如果当前的字符为 <，那么需要考虑下面的四种情况：

如果下一个字符为 /，那么说明我们遇到了一个结束标签。我们需要定位下一个 > 的位置 j，此时 code[i+2..j−1] 就是该结束标签的名称。
我们需要判断该名称与当前栈顶的名称是否匹配，如果匹配，说明名称的标签已经闭合，我们需要将当前栈顶的名称弹出。同时根据规则 1，我们
需要保证整个 code 被闭合标签包围，因此如果栈中已经没有标签，但是 j 并不是 code 的末尾，那么说明后续还会有字符，它们不被闭合标签
包围。

如果下一个字符为 !，那么说明我们遇到了一个 cdata，我们需要继续往后读 7 个字符，判断其是否为 [CDATA[。在这之后，我们定位下一个 
]]> 的位置 j，此时 code[i+9..j−1] 就是 cdata 中的内容，它不需要被解析，所以我们也不必进行任何验证。需要注意的是，根据规则 1，
栈中需要存在至少一个开放的标签。

如果下一个字符为大写字母，那么说明我们遇到了一个开始标签。我们需要定位下一个 > 的位置 j，此时 code[i+2..j−1] 就是该开始标签的
名称。我们需要判断该名称是否恰好由 1 至 9 个大写字母组成，如果是，说明该标签合法，我们需要将该名称放入栈顶。

除此之外，如果不存在下一个字符，或者下一个字符不属于上述三种情况，那么 code 是不合法的。

如果当前的字符为其它字符，那么根据规则 1，栈中需要存在至少一个开放的标签。
"""


class Solution(object):
    @staticmethod
    def isValid(code):
        """
        :type code: str
        :rtype: bool
        """
        n = len(code)
        tags = list()
        i = 0
        while i < n:
            if code[i] == "<":
                if i == n - 1:
                    return False
                if code[i + 1] == "/":
                    j = code.find(">", i)
                    if j == -1:
                        return False
                    tag_name = code[i + 2:j]
                    if not tags or tags[-1] != tag_name:
                        return False
                    tags.pop()
                    i = j + 1
                    if not tags and i != n:
                        return False
                elif code[i + 1] == "!":
                    if not tags:
                        return False
                    cdata = code[i + 2:i + 9]
                    if cdata != "[CDATA[":
                        return False
                    j = code.find("]]>", i)
                    if j == -1:
                        return False
                    i = j + 3
                else:
                    j = code.find(">", i)
                    if j == -1:
                        return False
                    tag_name = code[i + 1:j]
                    if not 1 <= len(tag_name) <= 9 or not all(ch.isupper() for ch in tag_name):
                        return False
                    tags.append(tag_name)
                    i = j + 1
            else:
                if not tags:
                    return False
                i += 1
        return not tags

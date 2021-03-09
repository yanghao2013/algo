# -*- coding: utf-8 -*-
"""
@Time   : 2021-03-10 00:00
@Author : Hao
"""

class Solution:

    """
    URL化。编写一种方法，将字符串中的空格全部替换为%20。假定该字符串尾部有足够的空间存放新增字符，并且知道字符串的“真实”长度。（注：用Java实现的话，请使用字符数组实现，以便直接在数组上操作。）
    链接：https://leetcode-cn.com/problems/string-to-url-lcci
    """
    def replaceSpaces(self, S: str, length: int) -> str:
        if length == 0:
            return ""
        t = S[0:length]
        s = ""
        for i in t:
            if i == ' ':
                s += "%20"
            else:
                s += i
        return s

    """
    给你一个字符串 s 和一个 长度相同 的整数数组 indices 。请你重新排列字符串 s ，其中第 i 个字符需要移动到 indices[i] 指示的位置。返回重新排列后的字符串。
    链接：https://leetcode-cn.com/problems/shuffle-string
    """
    def restoreString(self, s: str, indices: list[int]) -> str:
        if len(s) == 0:
            return ""
        tmp = ['0'] * len(s)
        for i in range(len(s)):
            tmp[indices[i]] = s[i]
        return "".join(tmp)
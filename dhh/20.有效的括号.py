#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#
# https://leetcode-cn.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (37.28%)
# Total Accepted:    64.4K
# Total Submissions: 172.6K
# Testcase Example:  '"()"'
#
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
#
# 有效字符串需满足：
#
#
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
#
#
# 注意空字符串可被认为是有效字符串。
#
# 示例 1:
#
# 输入: "()"
# 输出: true
#
#
# 示例 2:
#
# 输入: "()[]{}"
# 输出: true
#
#
# 示例 3:
#
# 输入: "(]"
# 输出: false
#
#
# 示例 4:
#
# 输入: "([)]"
# 输出: false
#
#
# 示例 5:
#
# 输入: "{[]}"
# 输出: true
#
#
class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True

        match_table = {'(': ')', '[': ']', '{': '}'}
        s_len = len(s) // 2 + 1
        stack_s = []
        for ch in s:
            if len(stack_s) > s_len:
                return False
            if not stack_s:
                stack_s.append(ch)
                continue

            if match_table.get(stack_s[-1]) == ch:
                stack_s.pop()
            else:
                stack_s.append(ch)

        return stack_s == []

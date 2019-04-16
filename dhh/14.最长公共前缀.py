#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#
# https://leetcode-cn.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (32.68%)
# Total Accepted:    70.2K
# Total Submissions: 214.4K
# Testcase Example:  '["flower","flow","flight"]'
#
# 编写一个函数来查找字符串数组中的最长公共前缀。
#
# 如果不存在公共前缀，返回空字符串 ""。
#
# 示例 1:
#
# 输入: ["flower","flow","flight"]
# 输出: "fl"
#
#
# 示例 2:
#
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
#
#
# 说明:
#
# 所有输入只包含小写字母 a-z 。
#
#
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        fronts = strs[0][:len(min(strs, key=lambda x: len(x)))]
        front_len = len(fronts)
        for el in strs[1:]:
            for idx in range(front_len, -1, -1):
                if el[:idx] == fronts[:idx]:
                    break
                front_len -= 1

            if not front_len:
                return ''
        return fronts[:front_len]

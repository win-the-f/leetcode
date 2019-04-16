#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#
# https://leetcode.com/problems/reverse-integer/description/
#
# algorithms
# Easy (25.23%)
# Total Accepted:    651.5K
# Total Submissions: 2.6M
# Testcase Example:  '123'
#
# Given a 32-bit signed integer, reverse digits of an integer.
#
# Example 1:
#
#
# Input: 123
# Output: 321
#
#
# Example 2:
#
#
# Input: -123
# Output: -321
#
#
# Example 3:
#
#
# Input: 120
# Output: 21
#
#
# Note:
# Assume we are dealing with an environment which could only store integers
# within the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose
# of this problem, assume that your function returns 0 when the reversed
# integer overflows.
#
#
class Solution:
    def reverse(self, x: int) -> int:
        if x <= -2 ** 31 or x >= 2 ** 31 - 1:
            return 0
        flag = False
        if x < 0:
            flag = True
            x = 0 - x

        v = 0
        while True:
            l = x // 10
            r = x - 10 * l
            v = v * 10 + x - 10 * l
            if l == 0:
                break
            x = l
        if flag:
            return 0 - v
        return v

#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#
# https://leetcode-cn.com/problems/reverse-integer/description/
#
# algorithms
# Easy (32.21%)
# Total Accepted:    108K
# Total Submissions: 335.1K
# Testcase Example:  '123'
#
# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
#
# 示例 1:
#
# 输入: 123
# 输出: 321
#
#
# 示例 2:
#
# 输入: -123
# 输出: -321
#
#
# 示例 3:
#
# 输入: 120
# 输出: 21
#
#
# 注意:
#
# 假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^31 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
#
#
class Solution:
    def reverse(self, x: int) -> int:
        if x > 2147483647 or x < -2147483648:
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


        if v > 2147483647 or v < -2147483648:
            return 0

        if flag:
            return 0 - v
        return v


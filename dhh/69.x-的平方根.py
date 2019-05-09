#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 1:
            return 0
        if x < 4:
            return 1
        l, m, r = 1, 2, 3
        while l < m:
            r = x // m
            l = m
            if l > r:
                l, r = r, l
            m = (l + r) // 2

        if m ** 2 > x:
            return m - 1
        return m

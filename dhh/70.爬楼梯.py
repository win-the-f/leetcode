#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#
class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return 1
        elif n < 3:
            return 2

        n1, n2 = 2, 1
        v = n1 + n2
        for idx in range(3, n):
            n1, n2 = v, n1
            v = n1 + n2

        return v

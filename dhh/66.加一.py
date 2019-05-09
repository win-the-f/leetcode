#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#
# https://leetcode-cn.com/problems/plus-one/description/
#
# algorithms
# Easy (38.14%)
# Total Accepted:    48K
# Total Submissions: 125.2K
# Testcase Example:  '[1,2,3]'
#
# 给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
#
# 最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。
#
# 你可以假设除了整数 0 之外，这个整数不会以零开头。
#
# 示例 1:
#
# 输入: [1,2,3]
# 输出: [1,2,4]
# 解释: 输入数组表示数字 123。
#
#
# 示例 2:
#
# 输入: [4,3,2,1]
# 输出: [4,3,2,2]
# 解释: 输入数组表示数字 4321。
#
#
#
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[0] == 0:
            return [1, ]
        nums = []
        while digits:
            num = digits.pop()
            if num == 9:
                nums.append(num)
            else:
                digits.append(num)
                break

        if digits:
            digits[-1] += 1
        else:
            digits.append(1)

        while nums:
            _ = nums.pop()
            digits.append(0)

        return digits


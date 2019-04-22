#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#
# https://leetcode-cn.com/problems/maximum-subarray/description/
#
# algorithms
# Easy (43.94%)
# Total Accepted:    51.3K
# Total Submissions: 115.7K
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
#
# 示例:
#
# 输入: [-2,1,-3,4,-1,2,1,-5,4],
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
#
#
# 进阶:
#
# 如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
#
#
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        max_value, temp = nums[0], nums[0]

        for value in nums[1:]:
            if temp <= 0:
                temp = value
            else:
                temp += value
            if temp > max_value:
                max_value = temp

        return max_value


#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n > 0:
            flag, t_nums = 1, []
            idx1, idx2 = 0, 0
            while idx2 < n:
                v = nums2[idx2]
                if t_nums:
                    if v > t_nums[0]:
                        flag = 0
                        v = t_nums[0]
                if idx1 < m:
                    if nums1[idx1] > v:
                        t_nums.append(nums1[idx1])
                    else:
                        idx1 += 1
                        continue

                nums1[idx1] = v
                idx2 += flag
                if not flag:
                    t_nums.pop(0)
                    flag = 1
                idx1 += 1
            if t_nums:
                self.merge(nums1, m + n - len(t_nums), t_nums, len(t_nums))

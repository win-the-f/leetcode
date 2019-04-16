#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#
# https://leetcode-cn.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (53.73%)
# Total Accepted:    60.3K
# Total Submissions: 112K
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# 将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
#
# 示例：
#
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
#
#
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        new_l = None
        while l1 or l2:
            if l1 and l2:
                if l1.val < l2.val:
                    t = ListNode(l1.val)
                    l1 = l1.next
                elif l1.val > l2.val:
                    t = ListNode(l2.val)
                    l2 = l2.next
                else:
                    t = ListNode(l2.val)
                    t.next = new_l
                    new_l = t
                    t = ListNode(l1.val)
                    l1 = l1.next
                    l2 = l2.next
            elif l1:
                t = ListNode(l1.val)
                l1 = l1.next
            elif l2:
                t = ListNode(l2.val)
                l2 = l2.next
            else:
                break
            t.next = new_l
            new_l = t

        n = None
        while new_l:
            t = ListNode(new_l.val)
            new_l = new_l.next
            t.next = n
            n = t
        return n


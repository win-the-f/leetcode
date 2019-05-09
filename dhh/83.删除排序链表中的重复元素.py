#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        new_head = None
        while 1:
            t = head
            head = head.next
            if head:
                if t.val != head.val:
                    t.next = new_head
                    new_head = t
            else:
                t.next = new_head
                new_head = t
                break
        while 1:
            if new_head:
                t = ListNode(new_head.val)
                t.next = head
                head = t
            else:
                break
            new_head = new_head.next
        return head


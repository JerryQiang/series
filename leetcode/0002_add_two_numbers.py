"""
难度: Medium
原题链接:https://leetcode.com/problems/two-sum
https://leetcode.com/problems/add-two-numbers/description/
内容描述:
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

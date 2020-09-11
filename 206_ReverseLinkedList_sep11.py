"""
link - https://leetcode.com/problems/reverse-linked-list/
Statement - Reverse a singly linked list.

Example:
    Input: 1->2->3->4->5->NULL
    Output: 5->4->3->2->1->NULL

"""



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        previous = None
        while head is not None:
            temp = head
            head = head.next
            temp.next = previous
            previous = temp
        return previous
            
            
        
# Last updated: 8/30/2025, 1:32:59 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            after = curr.next
            curr.next = prev
            prev = curr
            curr = after

        return prev
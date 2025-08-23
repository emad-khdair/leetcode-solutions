# Last updated: 8/23/2025, 5:23:02 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prev = None

        while current:
            after = current.next
            current.next = prev
            prev = current
            current = after

        return prev
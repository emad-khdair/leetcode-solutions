# Last updated: 8/17/2025, 2:04:32 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # If LL empty
        if not head or not head.next:
            return True

        # Find middle node using slow/fast pointers
        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # Reverse second half of list
        prev = None
        current = slow

        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        
        # Compare first half with second half of list

        first = head
        second = prev

        while second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
        return True

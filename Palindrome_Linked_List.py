from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        prev = None
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        start = slow
        while start:
            temp = start.next
            start.next = prev
            prev = start
            start = temp

        left = head
        right = prev
        while right:
            if right.val != left.val:
                return False
            left = left.next
            right = right.next

        return True

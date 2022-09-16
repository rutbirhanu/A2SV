from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = head

        while prev:
            while prev.next and prev.val == prev.next.val:
                prev.next = prev.next.next
            prev = prev.next

        return head

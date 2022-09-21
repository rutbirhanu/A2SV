from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        new = ListNode(0, head)
        a = new
        b = head
        for i in range(n):
            b = b.next

        while b:
            a = a.next
            b = b.next
        a.next = a.next.next

        return new.next


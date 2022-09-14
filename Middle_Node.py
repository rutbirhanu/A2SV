from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        size = 0
        current = head
        while current != None:
            current = current.next
            size += 1
        current = head
        for i in range(size // 2):
            current = current.next
        return current
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        size = 0
        start=1
        current = head
        while current != None:
            current = current.next
            size += 1
        current=head
        while start<size:
            current=current.next
            size-=1
            start+=1
        return current
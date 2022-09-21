from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        new = ListNode()
        another = new

        count = 0
        while l1 or l2 or count:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0
            total = num1 + num2 + count
            count = total // 10
            another.next = ListNode(total % 10)
            another = another.next
            l1 = l1.next if l1 else num1
            l2 = l2.next if l2 else num2

        return new.next

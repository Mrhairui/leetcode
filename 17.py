# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int):
        if not head:
            return None
        dummy = ListNode(0)
        dummy = head
        fast = dummy
        while n:
            fast = fast.next
            n = n - 1
        slow = dummy
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next





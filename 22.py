# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        p = dummy
        while head:
            if head and head.next:
                p.next = ListNode(head.next.val)
                p = p.next
                p.next = ListNode(head.val)
                head = head.next.next
            else:
                p.next = ListNode(head.val)
                head = head.next
            p = p.next

        return dummy.next


solution = Solution()
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)
a = solution.swapPairs(l1)
while a:
    print(a.val)
    a = a.next

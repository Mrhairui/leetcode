# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = ListNode(0)
        p = l3
        while l1 or l2:
            if l1 and l2:
                tmp1 = l1.val
                tmp2 = l2.val
                if tmp1 < tmp2:
                    p.next = ListNode(tmp1)
                    l1 = l1.next
                else:
                    p.next = ListNode(tmp2)
                    l2 = l2.next
            elif l1:
                p.next = ListNode(l1.val)
                l1 = l1.next
            elif l2:
                p.next = ListNode(l2.val)
                l2 = l2.next
            p = p.next
        return l3.next



solution = Solution()
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)
l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

a = solution.mergeTwoLists(l1, l2)
while a:
    print(a.val , '->')
    a = a.next







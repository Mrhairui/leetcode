# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = ListNode(0)
        while l1 != None or l2 != None:
            if l1.val <= l2.val:
                l3.next = l1
                l1 = l1.next
                l3 = l3.next
            else:
                l3.next = l2
                l2 = l2.next
                l3 = l3.next

        if l1 == None:
            while l2 != None:
                l3.next = l2
                l2 = l2.next
                l3 = l3.next
        elif l2 == None:
            l3.next = l1
            l1 = l1.next
            l3 = l3.next
        else:
            return l3
        return l3

solution = Solution()
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)
l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

a = solution.mergeTwoLists(l1, l2)







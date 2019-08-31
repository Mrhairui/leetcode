# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        tmp = head.next
        head.next = self.swapPairs(head.next.next)  # 类的递归
        tmp.next = head
        return tmp




solution = Solution()
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)
a = solution.swapPairs(l1)
while a:
    print(a.val)
    a = a.next
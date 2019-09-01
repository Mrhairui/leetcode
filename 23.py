# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def reverseKGroup(self, head, k: int):
        dummy = ListNode(0)
        p = dummy
        while True:
            stack = []
            count = k
            tmp = head
            while tmp and count:
                stack.append(tmp)
                tmp = tmp.next
                count -= 1
            if count:
                p.next = head
                break
            while stack:
                p.next = stack.pop()
                p = p.next
            p.next = tmp
            head = tmp
        return dummy.next


solution = Solution()
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)
a = solution.reverseKGroup(l1, 3)
while a:
    print(a.val)
    a = a.next







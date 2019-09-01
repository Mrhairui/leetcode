# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def reverseKGroup(self, head, k: int):
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        tail = dummy
        while True:
            count = k
            while count and tail:
                count -= 1
                tail = tail.next        # tail 用来跟踪序列里面的最后的值
            if not tail:  # tail为空说明不到一个序列退出即可
                break
            while pre.next != tail:  # pre初始值是0但是next每次都往后一个。
                cur = pre.next  # 每次初始化为pre的next
                pre.next = cur.next  # pre向前走一步，pre的作用很简单就是记录当前指针指到哪一个
                cur.next = tail.next  # cur是实际记录的指针，每次通过pre记录向前走一步，其next是通过tail,next来获得
                tail.next = cur  # 由于通过tail记录cur的next,所以cur每次赋给tail.next
            pre = head
            tail = head
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
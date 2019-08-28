# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def mergeKLists(self, lists) -> ListNode:
        import heapq
        dummy = ListNode(0)   # 这一步是为了生成一个头结点，便于存储以后生成的链表的头
        p = dummy
        head = []  #这个堆
        for i in range(len(lists)):   # 把所有链表的头放入到堆中
            if lists[i]:
                heapq.heappush(head, (lists[i].val, i))
                lists[i] = lists[i].next
        while head:                 # 只要堆不空就要继续往出弹出
            val, idx = heapq.heappop(head)  # 弹出四个链表头组成的堆中的最小值（四个链表本身是有序的）
            p.next = ListNode(val)  # 弹出的加入到链表中
            p = p.next  # 链表往前走一位
            if lists[idx]:  # 把三个链表中最小的头弹出（弹出后，后面又加入这个链表的下一个值）
                heapq.heappush(head, (lists[idx].val, idx))
                lists[idx] = lists[idx].next
        return dummy.next


solution = Solution()
l1 = ListNode(1)
l1.next = ListNode(4)
l1.next.next = ListNode(5)
l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)
l3 = ListNode(2)
l3.next = ListNode(6)
lists = [l1, l2, l3]

a = solution.mergeKLists(lists)


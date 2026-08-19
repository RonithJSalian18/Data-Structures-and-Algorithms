# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        res1 = []
        res2 = []

        cur = head
        while cur:
            if cur.val < x:
                res1.append(cur.val)
            else:
                res2.append(cur.val)
            cur = cur.next

        prev = tra = ListNode(0)
        for n in res1:
            prev.next = ListNode(n)
            prev = prev.next
        
        for n in res2:
            prev.next = ListNode(n)
            prev = prev.next

        return tra.next
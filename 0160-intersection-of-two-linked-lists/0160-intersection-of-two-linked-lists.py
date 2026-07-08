class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        sett = set()
        cur = headA

        while cur:
            sett.add(cur)
            cur = cur.next

        curB = headB
        while curB:
            if curB in sett:
                return curB
            curB = curB.next
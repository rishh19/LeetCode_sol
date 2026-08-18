class Solution:
    def removeElements(self, head, val):

        # Dummy node before the real head
        dummy = ListNode(0)
        dummy.next = head

        cur = dummy

        while cur.next:

            # If next node should be removed
            if cur.next.val == val:
                cur.next = cur.next.next

            else:
                cur = cur.next

        return dummy.next
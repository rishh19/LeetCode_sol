class Solution:
    def deleteMiddle(self, head):

        # Only one node
        if head.next == None:
            return None

        slow = head
        fast = head
        prev = None

        while fast and fast.next:

            prev = slow
            slow = slow.next
            fast = fast.next.next

        # slow is the middle node
        prev.next = slow.next

        return head
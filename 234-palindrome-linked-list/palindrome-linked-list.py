# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow=fast=head

        #finding middle node
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        #reverse the seocnd half only
        prev=None
        while slow:
            nxt=slow.next
            slow.next=prev
            prev=slow
            slow=nxt

        #comparing 1st half and 2nd half

        left=head
        right=prev

        while right:
            if left.val != right.val:
                return False
            left=left.next
            right=right.next
        return True
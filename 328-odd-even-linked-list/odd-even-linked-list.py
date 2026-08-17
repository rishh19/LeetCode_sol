# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
 

        if not head or not head.next:
            return head
        #2 pointers
        odd=head
        even=head.next
        even_head=even #store even head for future

        while even and even.next:
            #odd oints to other odd using even
            odd.next=even.next
            odd=odd.next

            #even points to other even using odd
            even.next=odd.next
            even=even.next

        #join the even part at end with odd part
        odd.next=even_head
        return head
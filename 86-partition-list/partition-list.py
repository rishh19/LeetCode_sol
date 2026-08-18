# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        #dummy nodes
        sDummy=ListNode(0)
        bDummy=ListNode(0)

        #two pointers for both dummy
        s=sDummy
        b=bDummy

        #go until curr is not none
        curr=head
        while curr:
            if curr.val<x:
                #put in sdummy
                s.next=curr
                s=s.next
            else:
                #put in bdummy
                b.next=curr
                b=b.next
            curr=curr.next

        # Connect small list to big list
        s.next = bDummy.next

        # End the big list
        b.next = None

        return sDummy.next
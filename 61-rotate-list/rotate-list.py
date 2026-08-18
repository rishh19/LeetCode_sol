# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #0/1 node only
        if head==None or head.next==None:
            return head

        #find list length
        n=1
        tail=head
        while tail.next:
            tail=tail.next
            n+=1
        
        #reduce to find k
        k=k%n
        if k==0:
            return head

        #make circle
        tail.next=head

        #find cut i.e. new head
        curr=head
        for _ in range(n-k-1):
            curr=curr.next

        #new head after curr
        head=curr.next

        #break circle
        curr.next=None
        return head

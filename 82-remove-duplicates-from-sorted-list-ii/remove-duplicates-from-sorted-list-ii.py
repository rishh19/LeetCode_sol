# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next = head

        prev = dummy
        curr= head

        #traverse till curr is present
        while curr:
            #if duplicate comes
            if curr.next and curr.val==curr.next.val:
                #keep going until duplicates are coming
                while curr.next and curr.val==curr.next.val:
                    curr=curr.next
                prev.next=curr.next
            else:
                prev=prev.next
            curr=curr.next
        return dummy.next

            
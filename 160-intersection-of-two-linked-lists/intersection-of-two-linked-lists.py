# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        #two pointers 
        #after reaching the end of one list switch it to another list

        a=headA
        b=headB

        #loop till they are not same
        while a!=b:
            if a: #a is not none then move
                a=a.next
            else: #swtich to b list
                a=headB
            if b: #b is not none then move
                b=b.next
            else: #swtich to a list
                b=headA
        return a
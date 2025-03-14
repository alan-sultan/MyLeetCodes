# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h = head
        while h.next:
            h.next = ListNode(gcd(h.val, h.next.val), h.next)
            h = h.next.next
        return head
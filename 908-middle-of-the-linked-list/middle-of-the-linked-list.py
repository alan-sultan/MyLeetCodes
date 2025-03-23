# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = 0
        temp = head
        while temp:
            temp = temp.next
            l += 1
        l = l // 2
        while l:
            head = head.next
            l -= 1
        return head

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        heap = []
        for ls in lists:
            while ls:
                heappush(heap,ls.val)
                ls = ls.next
        cur = dummy
        while heap:
            cur.next = ListNode(heappop(heap))
            cur = cur.next
        return dummy.next

        
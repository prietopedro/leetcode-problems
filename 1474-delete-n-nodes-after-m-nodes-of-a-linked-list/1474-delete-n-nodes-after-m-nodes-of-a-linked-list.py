# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        curr = head
        while curr is not None:
            keep = m - 1
            delete = n + 1
            while curr is not None and keep:
                curr = curr.next
                keep -= 1
            if not curr: break
            prev = curr
            while curr is not None and delete:
                curr = curr.next
                delete -= 1
            prev.next = curr
        return head


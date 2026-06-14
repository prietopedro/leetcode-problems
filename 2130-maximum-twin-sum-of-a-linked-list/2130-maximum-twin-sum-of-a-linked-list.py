# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        seen = []
        curr = head
        max_sum = 0

        while curr:
            seen.append(curr.val)
            curr = curr.next

        for i in range(len(seen) // 2):
            max_sum = max(max_sum, seen[i] + seen[-i - 1])
        return max_sum


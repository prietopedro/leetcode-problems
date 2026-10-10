# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        q_left, q_right = deque([p]), deque([q])
        while q_left and q_right:
            for _ in range(len(q_left)):
                left,right = q_left.popleft(), q_right.popleft()
                if not left and not right:
                    continue
                if not left or not right:
                    return False
                if left.val != right.val:
                    return False
                q_left.append(left.left)
                q_left.append(left.right)
                q_right.append(right.left)
                q_right.append(right.right)
        return True
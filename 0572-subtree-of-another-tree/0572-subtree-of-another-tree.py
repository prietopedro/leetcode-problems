# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        main_q = deque([root])
        while main_q:
            sub_q = deque([(main_q.popleft(), subRoot)])
            valid = True
            first = True
            while sub_q:
                main,sub = sub_q.popleft()
                if first:
                    if main:
                        main_q.append((main.left))
                        main_q.append((main.right))
                    first = False
                
                if not main and not sub:
                    continue
                if not main or not sub or main.val != sub.val:
                    valid = False
                    break
                sub_q.append((main.left,sub.left))
                sub_q.append((main.right, sub.right))
            if valid:
                return True
        return False
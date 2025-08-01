# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        q = deque([(root,0)])
        output = defaultdict(list)
        min_level = inf
        max_level = -inf
        while q:
            node,level = q.popleft()
            min_level,max_level = min(min_level,level),max(max_level,level)
            output[level].append(node.val)
            if node.left:
                q.append((node.left,level - 1))
            if node.right:
                q.append((node.right,level + 1))
        length = max_level - min_level + 1
        real_output = [[] for _ in range(length)]

        for key in output.keys():
            real_output[key - min_level] = output[key]
        return real_output
        

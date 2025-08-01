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
        store = defaultdict(list)
        while q:
            for _ in range(len(q)):
                curr,level = q.popleft()
                store[level].append(curr.val)
                if curr.left:
                    q.append((curr.left,level - 1))
                if curr.right:
                    q.append((curr.right,level + 1))
        
        min_index = min(store.keys())
        max_index = max(store.keys())
        output = []
        for i in range(min_index,max_index + 1):
            output.append(store[i])
        return output
            
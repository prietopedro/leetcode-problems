# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        # if not inorder:
        #     return None
        # node = TreeNode(preorder[0])
        # left = inorder.index(preorder[0])
        # node.left = self.buildTree(preorder[1:],inorder[:left])
        # node.right = self.buildTree(preorder[1 + left:],inorder[left + 1:])
        # return node
        def buildTreeHelper(preorderS,preorderE,inorderS,inorderE):
            if preorderS > preorderE or inorderS > inorderE:
                return None
            node = TreeNode(preorder[preorderS])

            mid = inorder.index(preorder[preorderS], inorderS, inorderE + 1)
            left_size = mid - inorderS

            node.left = buildTreeHelper(
                preorderS + 1,
                preorderS + left_size,
                inorderS,
                mid - 1
            )

            node.right = buildTreeHelper(
                preorderS + left_size + 1,
                preorderE,
                mid + 1,
                inorderE
            )
            return node
        return buildTreeHelper(0,len(preorder) - 1,0,len(inorder) - 1)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def a_tree(root):
            if (root == None):
                return 0
            l = a_tree(root.left)
            r = a_tree(root.right)
            return 1 + l + r
        return a_tree(root)

        
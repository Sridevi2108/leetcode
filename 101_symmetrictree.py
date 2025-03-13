# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def ismirror(left,right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            return (left.val==right.val and ismirror(left.left,right.right)and ismirror(left.right,right.left))
        return ismirror(root.left,root.right)

def build_tree():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)
    return root
solution = Solution()
tree = build_tree()
print(solution.isSymmetric(tree))
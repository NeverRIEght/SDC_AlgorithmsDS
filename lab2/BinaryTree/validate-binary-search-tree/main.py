# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, low, high):
            if node is None:
                return True

            # If current value is out of range - invalid tree
            if not (low < node.val < high):
                return False

            # check left and right with updated range
            return (validate(node.left, low, node.val)
                    and validate(node.right, node.val, high))

        # float inf stand for positive infinity.
        # float -inf stand for negative infinity.
        return validate(root, float('-inf'), float('inf'))

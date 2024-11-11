# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def traverse(node, level):
            if node is None:
                return

            # create new list for a level if not exists
            if len(res) == level:
                res.append([])

            # append current node as a node on current level
            res[level].append(node.val)

            # continue for left and right nodes with incremented level
            traverse(node.left, level + 1)
            traverse(node.right, level + 1)

        res = []
        traverse(root, 0)
        return res
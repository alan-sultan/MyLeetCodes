# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        qu = deque([root])
        while qu:
            node = qu.popleft()
            if node.val != root.val:
                return False
            if node.left:
                qu.append(node.left)
            if node.right:
                qu.append(node.right)
        return True

        # curr = root
        # def rec(curr):
        #     if not curr:
        #         return True
        #     if curr.val != root.val:
        #         return False
        #     return rec(curr.left)
        #     return rec(curr.right)
        
        # return rec(curr)

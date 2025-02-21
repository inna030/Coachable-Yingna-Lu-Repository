# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        dic=defaultdict(int)
        def dfs(node,level):
            if not node:
                return 
            dic[level]+=node.val
            dfs(node.left,level+1)
            dfs(node.right,level+1)

        dfs(root,1)
        return max(dic,key=dic.get)

        

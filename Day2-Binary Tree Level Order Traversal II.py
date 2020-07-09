'''

### Question ###

Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:

[
  [15,7],
  [9,20],
  [3]
]

### Solution ###

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        tree = []
        if not root:
            return tree
        Q = []
        Q.append(root)
        while len(Q) > 0 :
            n = len(Q)
            branch = []
            
            for i in range(n):
                node = Q.pop(0)
                branch.append(node.val)
                if node.left != None :  Q.append(node.left)
                if node.right != None : Q.append(node.right)
            tree.insert(0,branch)
        return tree

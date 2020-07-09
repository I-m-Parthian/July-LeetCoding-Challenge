/*

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



*/

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> levelOrderBottom(TreeNode* root) 
    {
        vector<vector<int>> tree;
        if(!root)
            return tree;
        queue<TreeNode*> Q;
        Q.push(root);
        while(!Q.empty())
        {
            int n = Q.size();
            vector<int> branch(n);
            
            for(int i=0;i<n;i++)
            {
                TreeNode* node = Q.front();
                Q.pop();
                branch[i] = node->val;
                if(node->left) Q.push(node->left);
                if(node->right) Q.push(node->right);
            }
            tree.push_back(branch);
        }
        reverse(tree.begin(),tree.end());
        return tree;
    }
};

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
    TreeNode* invertTree(TreeNode* root) {
        return invert(root);
    }

private:
    TreeNode* invert(TreeNode* node) {
        if (!node) {
            return node;
        }

        TreeNode* left = node->left;
        TreeNode* right = node->right;

        node->left = invert(right);
        node->right = invert(left);
        
        return node;
    }
};

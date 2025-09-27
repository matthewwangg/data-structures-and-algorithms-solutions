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
    bool isValidBST(TreeNode* root) {
        return validate(root, std::numeric_limits<long long>::min(), std::numeric_limits<long long>::max());
    }

private:
    bool validate(TreeNode* node, long long minimum, long long maximum) {
        if (!node) {
            return true;
        }

        return node->val > minimum && node->val < maximum && validate(node->left, minimum, node->val) && validate(node->right, node->val, maximum);
    }
};

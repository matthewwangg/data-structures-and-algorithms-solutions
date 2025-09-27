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
    bool isBalanced(TreeNode* root) {
        return explore(root).first;
    }

private:
    std::pair<bool, int> explore(TreeNode* node) {
        if (!node) {
            return std::make_pair(true, 0);
        }

        std::pair<bool, int> left = explore(node->left);
        std::pair<bool, int> right = explore(node->right);

        return std::make_pair(left.first && right.first && std::abs(left.second - right.second) <= 1, std::max(left.second, right.second) + 1);
    }
};

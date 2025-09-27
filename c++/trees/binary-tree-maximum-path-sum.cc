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
    int maxPathSum(TreeNode* root) {
        return findSum(root).first;
    }

private:
    std::pair<int, int> findSum(TreeNode* node) {
        if (!node) {
            return std::make_pair(std::numeric_limits<int>::min(), std::numeric_limits<int>::min());
        }

        std::pair<int, int> left = findSum(node->left);
        std::pair<int, int> right = findSum(node->right);

        return std::make_pair(std::max({left.first, right.first, std::max(left.second, 0) + std::max(right.second, 0) + node->val}), std::max({std::max(left.second, 0) + node->val, std::max(right.second, 0) + node->val}));
    }
};

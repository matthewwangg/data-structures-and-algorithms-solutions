/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        return std::get<0>(find(root, p, q));
    }

private:
    std::tuple<TreeNode*, bool, bool> find(TreeNode* node, TreeNode* p, TreeNode* q) {
        if (!node) {
            return std::make_tuple(nullptr, false, false);
        }

        std::tuple<TreeNode*, bool, bool> left = find(node->left, p, q);
        std::tuple<TreeNode*, bool, bool> right = find(node->right, p, q);

        if (std::get<0>(left)) {
            return std::make_tuple(std::get<0>(left), true, true);
        }

        if (std::get<0>(right)) {
            return std::make_tuple(std::get<0>(right), true, true);
        }

        if (node == p) {
            if (std::get<2>(left) || std::get<2>(right)) {
                return std::make_tuple(node, true, true);
            }
        }

        if (node == q) {
            if (std::get<1>(left) || std::get<1>(right)) {
                return std::make_tuple(node, true, true);
            }
        }

        if ((std::get<2>(left) || std::get<2>(right)) && (std::get<1>(left) || std::get<1>(right))) {
            return std::make_tuple(node, true, true);
        }

        return std::make_tuple(nullptr, std::get<1>(left) || std::get<1>(right) || node == p, std::get<2>(left) || std::get<2>(right) || node == q);
    }
};

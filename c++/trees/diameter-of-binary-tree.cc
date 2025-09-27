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
    int diameterOfBinaryTree(TreeNode* root) {
        return explore(root).first;
    }

private:
    std::pair<int, int> explore(TreeNode* node) {
        if (!node) {
            return std::make_pair(0, 0);
        }
        
        std::pair<int, int> left = explore(node->left);
        std::pair<int, int> right = explore(node->right);

        return std::make_pair(std::max(left.first, std::max(right.first, left.second + right.second)), std::max(left.second, right.second) + 1);
    }
};

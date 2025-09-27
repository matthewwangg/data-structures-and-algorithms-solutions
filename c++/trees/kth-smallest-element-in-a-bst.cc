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
    int kthSmallest(TreeNode* root, int k) {
        getValues(root);
        return elements_[k-1];
    }

private:
    void getValues(TreeNode* node) {
        if (!node) {
            return;
        }

        getValues(node->left);
        elements_.push_back(node->val);
        getValues(node->right);
    }

    std::vector<int> elements_;
};

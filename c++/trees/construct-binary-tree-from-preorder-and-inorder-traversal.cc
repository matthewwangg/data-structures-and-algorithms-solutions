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
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        std::unordered_map<int, int> indexes;
        for (int i = 0; i < inorder.size(); ++i) {
            indexes[inorder[i]] = i;
        }

        return construct(preorder, indexes);
    }

private:
    TreeNode* construct(std::vector<int>& elements, std::unordered_map<int, int>& indexes) {
        if (elements.empty()) {
            return nullptr;
        }

        TreeNode* node = new TreeNode(elements[0]);

        std::vector<int> left;
        std::vector<int> right;

        for (int i = 1; i < elements.size(); ++i) {
            if (indexes[elements[i]] > indexes[elements[0]]) {
                right.push_back(elements[i]);
            } else {
                left.push_back(elements[i]);
            }
        }

        node->left = construct(left, indexes);
        node->right = construct(right, indexes);

        return node;
    }
};

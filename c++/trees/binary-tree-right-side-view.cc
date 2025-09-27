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
    vector<int> rightSideView(TreeNode* root) {
        std::queue<std::pair<TreeNode*, int>> q;
        q.push(std::make_pair(root, 0));
        
        std::vector<int> levels;
        while (q.size() > 0) {
            std::pair<TreeNode*, int> node = q.front();
            q.pop();

            if (!node.first) {
                continue;
            }

            if (node.second == levels.size()) {
                levels.push_back(0);
            }

            levels[node.second] = node.first->val;

            q.push(std::make_pair(node.first->left, node.second + 1));
            q.push(std::make_pair(node.first->right, node.second + 1));
        }

        return levels;
    }
};

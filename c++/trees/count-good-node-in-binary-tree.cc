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
    int goodNodes(TreeNode* root) {
        return count(root, std::numeric_limits<int>::min());
    }

private:
    int count(TreeNode* node, int maximum) {
        if (!node) {
            return 0;
        }

        int answer = 0;
        if (node->val >= maximum) {
            answer += 1;
        }

        answer += count(node->left, std::max(node->val, maximum));
        answer += count(node->right, std::max(node->val, maximum));

        return answer;
    } 
};

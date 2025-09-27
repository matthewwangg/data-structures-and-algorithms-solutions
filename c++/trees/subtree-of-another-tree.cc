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
    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
        std::queue<TreeNode*> q;
        q.push(root);
        while (q.size() != 0) {
            TreeNode* node = q.front();
            q.pop();

            if (!node) {
                continue;
            }

            if (node->val == subRoot->val) {
                if (compare(node, subRoot)) {
                    return true;
                }
            }

            q.push(node->left);
            q.push(node->right);
        }
        return false;
    }

private:
    bool compare(TreeNode* p, TreeNode* q) {
        if (!p && !q) {
            return true;
        }

        if (!p || !q) {
            return false;
        }

        return p->val == q->val && compare(p->left, q->left) && compare(p->right, q->right);
    }
};

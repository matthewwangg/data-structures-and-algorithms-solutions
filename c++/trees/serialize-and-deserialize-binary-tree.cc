/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Codec {
public:

    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        std::string encoding = encode(root);
        return encoding.substr(0, encoding.size()-1);
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        std::vector<std::string> tokens;
        std::stringstream ss(data);
        std::string token;

        while (ss >> token) {
            tokens.push_back(token);
        }

        std::reverse(tokens.begin(), tokens.end());

        return construct(tokens);
    }

private:
    string encode(TreeNode* node) {
        if (!node) {
            return "None ";
        }

        std::string encoding = std::to_string(node->val) + " ";
        encoding += encode(node->left);
        encoding += encode(node->right);

        return encoding;
    }

    TreeNode* construct(std::vector<std::string>& tokens) {
        if (tokens.back() == "None") {
            tokens.pop_back();
            return nullptr;
        }

        TreeNode* node = new TreeNode(std::stoi(tokens.back()));
        tokens.pop_back();
        node->left = construct(tokens);
        node->right = construct(tokens);

        return node;
    }
};

// Your Codec object will be instantiated and called as such:
// Codec ser, deser;
// TreeNode* ans = deser.deserialize(ser.serialize(root));

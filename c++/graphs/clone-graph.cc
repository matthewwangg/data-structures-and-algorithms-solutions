/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
public:
    Node* cloneGraph(Node* node) {
        if (!node) {
            return nullptr;
        }

        std::unordered_map<Node*, Node*> mapping;
        std::queue<Node*> q;
        q.push(node);

        while (q.size() > 0) {
            Node* current = q.front();
            q.pop();

            if (!mapping[current]) {
                mapping[current] = new Node(current->val);
            }

            for (Node* neighbor : current->neighbors) {
                if (!mapping[neighbor]) {
                    mapping[neighbor] = new Node(neighbor->val);
                    q.push(neighbor);
                }
                mapping[current]->neighbors.push_back(mapping[neighbor]);
            }
        }

        return mapping[node];
    }
};

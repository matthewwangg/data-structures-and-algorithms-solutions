/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        if (!head) {
            return nullptr;
        }

        std::unordered_map<Node*, Node*> node_mapping = {{head, new Node(head->val)}};
        Node* pointer = head;

        while (pointer->next) {
            node_mapping[pointer]->next = new Node(pointer->next->val);
            node_mapping[pointer->next] = node_mapping[pointer]->next;
            pointer = pointer->next;
        }

        pointer = head;
        while (pointer) {
            node_mapping[pointer]->random = node_mapping[pointer->random];
            pointer = pointer->next;
        }

        return node_mapping[head];
    }
};

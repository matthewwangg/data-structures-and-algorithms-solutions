/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        std::priority_queue<std::pair<int, ListNode*>> pq;

        ListNode* head = new ListNode();
        ListNode* pointer = head;

        for (ListNode* node : lists) {
            if (!node) {
                continue;
            }
            pq.push(std::make_pair(-node->val, node));
        }

        while (pq.size() > 0) {
            std::pair<int, ListNode*> element = pq.top();
            pq.pop();

            ListNode* next_element = element.second->next;

            pointer->next = element.second;            
            pointer = pointer->next;
            pointer->next = nullptr;

            if (next_element) {
                pq.push(std::make_pair(-next_element->val, next_element));
            }
        }

        return head->next;
    }
};

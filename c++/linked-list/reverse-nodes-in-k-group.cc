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
    ListNode* reverseKGroup(ListNode* head, int k) {
        std::vector<ListNode*> groups;
        int count = 0;

        ListNode* group = head;
        ListNode* pointer = head;
        while (pointer) {
            count += 1;
            if (count % k == 0) {
                groups.push_back(group);
                group = pointer->next;
                pointer->next = nullptr;
                pointer = group;
            } else {
                pointer = pointer->next;
            }
        }

        groups.push_back(group);

        ListNode* answer = new ListNode();
        pointer = answer;
        for (ListNode* node : groups) {
            while (pointer->next) {
                pointer = pointer->next;
            }

            if (checkListLength(node) == k) {
                pointer->next = reverseList(node);
            } else {
                pointer->next = node;
            }
        }

        return answer->next;
    }

private:
    int checkListLength(ListNode* head) {
        int length = 0;
        ListNode* pointer = head;
        while (pointer) {
            length += 1;
            pointer = pointer->next;
        }
        return length;
    }

    ListNode* reverseList(ListNode* head) {
        if (!head || !head->next) {
            return head;
        }

        ListNode* prev = head;
        ListNode* curr = prev->next;

        while (curr) {
            ListNode* next = curr->next;
            curr->next = prev;
            prev = curr;
            curr = next;
        }
        head->next = nullptr;

        return prev;
    }
};

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
    void reorderList(ListNode* head) {
        int count = 0;
        ListNode* pointer = head;
        while (pointer) {
            pointer = pointer->next;
            count += 1;
        }

        pointer = head;
        if (count % 2 == 0) {
            count /= 2;
            count -= 1;
        } else {
            count /= 2;
        }
        while (count > 0) {
            count -= 1;
            pointer = pointer->next;
        }

        ListNode* first = head;
        ListNode* second = reverseList(pointer->next);

        pointer->next = nullptr;
        
        pointer = new ListNode();
        while (first || second) {
            if (first) {
                pointer->next = first;
                first = first->next;
                pointer = pointer->next;
                pointer->next = nullptr;
            }

            if (second) {
                pointer->next = second;
                second = second->next;
                pointer = pointer->next;
                pointer->next = nullptr;
            }
        }
    }

private:
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

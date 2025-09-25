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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* reverse = reverseList(head);
        ListNode* pointer = reverse;

        if (n == 1) {
            return reverseList(reverse->next);
        }

        int count = 0;
        while (count < n - 2) {
            pointer = pointer->next;
            count += 1;
        }

        if (pointer->next) {
            pointer->next = pointer->next->next;
        } else {
            pointer->next = nullptr;
        }

        return reverseList(reverse);
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

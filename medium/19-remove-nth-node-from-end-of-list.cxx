/**
 * Definition for singly-linked list.
**/
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        auto dummy = new ListNode();
        dummy->next = head;
        // Left begins at one position before head
        auto left = dummy;
        auto right = head;
        // Move right n distance from left
        while(n != 0 and right) {
            right = right->next;
            --n;
        }
        // Move right to one position after the last element which makes it nullptr
        // left will be one postition before the target
        while (right) {
            right = right->next;
            left = left->next;
        }
        // Reomve target
        left->next = left->next->next;
        return dummy->next;
    }
};

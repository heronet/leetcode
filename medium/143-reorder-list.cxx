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
    void reorderList(ListNode* head) {
        auto first = head;
        auto slow = head;
        auto fast = head;

        while(fast && fast->next) {
            slow = slow->next;
            fast = fast->next->next;
        }
        ListNode* prev = nullptr;
        auto current = slow->next;
        while(current) {
            auto temp = current->next;
            current->next = prev;
            prev = current;
            current = temp;
        }
        slow->next = nullptr;
        while(prev) {
            auto temp1 = first->next;
            auto temp2 = prev->next;
            first->next = prev;
            prev->next = temp1;
            first = temp1;
            prev = temp2;
        }
    }
}; 

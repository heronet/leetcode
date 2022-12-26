#include <iostream>
/**
 * Definition for singly-linked list.
 *
 **/
struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution
{
public:
    ListNode *addTwoNumbers(ListNode *l1, ListNode *l2)
    {
        auto dummy = new ListNode();
        auto curr = dummy;
        int carry = 0;

        while (l1 || l2 || carry)
        {
            int val1 = l1 ? l1->val : 0;
            int val2 = l2 ? l2->val : 0;
            int val = val1 + val2 + carry;
            carry = val / 10;
            val = val % 10;
            auto newnode = new ListNode(val);
            curr->next = newnode;
            curr = curr->next;
            l1 = l1 ? l1->next : nullptr;
            l2 = l2 ? l2->next : nullptr;
        }
        return dummy->next;
    }
};
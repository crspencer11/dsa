/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode dummy = new ListNode(0);
        ListNode current = dummy;
        dummy.next = head;  
        int linkedListLength = findLength(head); 
        int intendedNode = linkedListLength - n;
        int counter = 0;
        while (counter < intendedNode) {
            counter++;
            current = current.next;
        }
        current.next = current.next.next;
        return dummy.next;
    }

    public int findLength(ListNode head) {
        int len = 0;
        ListNode curr = head;
        while (curr != null) {
            len++;
            curr = curr.next;
        }
        return len;
    }
}


class Solution {
    public ListNode middleNode(ListNode head) {
        int len = findMiddle(head);
        for(int i=0; i<len/2; i++) {
            head = head.next;
        }
        return head;
    }
    
    private int findMiddle(ListNode head) {
        int len=0;
        while(head != null) {
            head = head.next;
            len++;
        }
        return len;
    }
}

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        stack = []
        curr = head
        while curr:
            stack.append(curr)
            curr = curr.next
        
        n = len(stack)
        reset_curr = head
        for i in range(n // 2):
            tail = stack.pop()
            next_node = reset_curr.next
            reset_curr.next = tail
            tail.next = next_node
            reset_curr = next_node
        reset_curr.next = None


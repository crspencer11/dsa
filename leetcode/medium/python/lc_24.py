def swap_pairs(head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        else:
            new_head = head.next
            prev = None
            curr = head
            while curr and curr.next:
                next_node = curr.next
                if prev:
                    prev.next = next_node
                curr.next = next_node.next
                next_node.next = curr
                prev = curr
                curr = curr.next
            return new_head

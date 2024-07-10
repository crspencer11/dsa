def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2
        leftover = 0
        head = ListNode()
        curr = head
        while curr1 or curr2 or leftover:
            val1 = curr1.val if curr1 else 0
            val2 = curr2.val if curr2 else 0
            added = val1 + val2 + leftover
            leftover = added // 10
            curr.next = ListNode(added % 10)
            curr = curr.next
            if curr1:
                curr1 = curr1.next
            if curr2:
                curr2 = curr2.next
        return head.next

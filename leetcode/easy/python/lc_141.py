def hasCycle(head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        if head.next is None:
            return False
        else:
            d = {}
            curr = head
            index = 0
            while curr:
                d[curr] = index
                index += 1
                curr = curr.next
                if curr in d:
                    return True
            return False

import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
def merge_k_lists(lists):
    min_heap = []
    
    for idx, node in enumerate(lists):
        if node:
            heapq.heappush(min_heap, (node.val, idx, node))
    
    dummy = ListNode(0)
    current = dummy

    while min_heap:
        idx, node = heapq.heappop(min_heap)
        current.next = node
        current = current.next
        if node.next:
            heapq.heappush(min_heap, (node.next.val, idx, node.next))
    
    return dummy.next

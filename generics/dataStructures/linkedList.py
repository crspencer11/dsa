class LinkedList:
    
    class Node:
        def __init__(self, val=None):
            self.val = val
            self.next = None
    
    def __init__(self):
        self.head = None
    
    def get(self, index: int) -> int:
        curr = self.head
        count = 0
        while curr is not None:
            if count == index:
                return curr.val
            count += 1
            curr = curr.next
        return -1
    
    def insertHead(self, val: int) -> None:
        new_node = self.Node(val)
        new_node.next = self.head
        self.head = new_node
    
    def insertTail(self, val: int) -> None:
        new_node = self.Node(val)
        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
    
    def remove(self, index: int) -> bool:
        if not self.head:
            return False
        
        if index == 0:
            self.head = self.head.next
            return True
        
        curr = self.head
        prev = None
        count = 0
        while curr is not None:
            if count == index:
                prev.next = curr.next
                return True
            prev = curr
            curr = curr.next
            count += 1
        return False
    
    def getValues(self) -> list[int]:
        values = []
        curr = self.head
        while curr is not None:
            values.append(curr.val)
            curr = curr.next
        return values


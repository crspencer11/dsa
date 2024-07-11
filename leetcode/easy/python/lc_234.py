def isPalindrome(head: Optional[ListNode]) -> bool:
        lst = traverse(head)
        print(lst)
        j = -1
        for i in range(len(lst)//2):
            if lst[i] != lst[j]:
                return False
            j -= 1
        return True
    
def traverse(head):
    curr = head
    final = []
    while curr:
        final.append(curr.val)
        curr = curr.next
    return final
func getIntersectionNode(headA, headB *ListNode) *ListNode {
    if headA == nil || headB == nil { 
        return nil
    }
    pointerA := headA
    pointerB := headB
    for pointerA != pointerB {
        if pointerA != nil {
            pointerA = pointerA.Next
        } else {
            pointerA = headB
        }
        if pointerB != nil {
            pointerB = pointerB.Next
        } else {
            pointerB = headA
        }
    }
    return pointerA
}


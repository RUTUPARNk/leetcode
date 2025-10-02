class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None

        # --- STEP 1: Reverse the list ---
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        # After this, 'prev' is the new head (L_n)

        # --- STEP 2: Remove the Nth node from the START of the reversed list ---
        # Initialize a dummy node to handle the case where the head (L_n) is removed.
        dummy = ListNode()
        temp = dummy
        temp.next = prev 
        
        # Move temp to the (N-1) position (i.e., the node BEFORE the target)
        for _ in range(n - 1):
            temp = temp.next
            
        # Perform the deletion: skip the Nth node
        temp.next = temp.next.next

        # --- STEP 3: Reverse the list back to the original order ---
        # The head of the list to reverse is now dummy.next
        prev = None
        curr = dummy.next
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            
        # 'prev' now holds the head of the final, corrected list.
        return prev

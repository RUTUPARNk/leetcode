"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # Hash map (dictionary) to store the mapping: Old Node -> New Node
        old_to_new = {}

        # --- STEP 1: Create all new nodes and build the map ---
        curr = head
        while curr:
            # Create the copy of the node's value
            new_node = Node(curr.val)
            # Store the mapping: Old Node Object -> New Node Object
            old_to_new[curr] = new_node
            curr = curr.next

        # --- STEP 2: Set the next and random pointers on the new nodes ---
        curr = head
        while curr:
            # Get the new node copy corresponding to the current old node
            new_node = old_to_new[curr]
            
            # Set .next: Look up the copy of curr.next in the map. 
            # Use .get() to safely return None if curr.next is None (end of list).
            new_node.next = old_to_new.get(curr.next, None)
            
            # Set .random: Look up the copy of curr.random in the map.
            # Use .get() to safely return None if curr.random is None.
            new_node.random = old_to_new.get(curr.random, None)
            
            curr = curr.next

        # --- STEP 3: Return the head of the new list ---
        # The head of the new list is the copy of the original head
        return old_to_new[head]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode() # build the merged list
        # dummy -> [0] <- node
        # dummy will always point to the start of the merged list
        # node is a pointer we use to keep track of the current tail of the merged list

        while list1 and list2: # as long as both lists still have nodes
            if list1.val < list2.val: # whichever is smaller gets attached to the merged list
                node.next = list1 # attach list1's node to the merged list
                list1 = list1.next # move list1 forward to its next node
            else:
                node.next = list2 # attach list2's node
                list2 = list2.next # move list2 forward
            node = node.next # after attaching a node, move the node pointer forward too.
            # so node always points to the last node in the merged list so far.

        node.next = list1 or list2
        # at this point, one of the lists is empty
        # the remaining nodes in the other list are already sorted, so we can attach them all at once

        return dummy.next
        
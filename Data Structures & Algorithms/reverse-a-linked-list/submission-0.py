# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Example list: 0 -> 1 -> 2 -> 3 -> None
        prev, curr = None, head

        while curr: # 第一輪迴圈，curr 目前是 0
            temp = curr.next # save next node in temp: 把 0 的下一個節點 1 暫存起來（否則把線剪斷後會找不到後面）。
            curr.next = prev # reverse the link: 將 0 的指標指向 prev（也就是 None），此時 0 的箭頭被轉向了：0 -> None。
            prev = curr # move prev forward: 把 prev (None) 移到目前節點 0。
            curr = temp # move curr forward: 把 curr (0) 移到下一個節點 1。
        
        return prev

        
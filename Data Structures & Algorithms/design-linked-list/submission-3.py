# singly linked list
# Shape: dummy -> 1 -> 2 -> 3 -> None
# The real list starts at dummy.next. Without a dummy head, addAtHead and deleteAtIndex(0) need special handling.

# Main idea for operations:
# To insert or delete at index i, you first find the node before that index:

# for addAtIndex(i, val), find node at index i - 1
# for deleteAtIndex(i), find node at index i - 1
# Then update pointers.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.dummy = ListNode(0)
        self.size = 0        

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        # 從第一個真正節點開始
        cur = self.dummy.next
        # 往後走 index 次
        for _ in range(index):
            cur = cur.next
        return cur.val        

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)        

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)        

    # 先找到插入位置前面的節點 prev，再把新節點接進去
    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        
        # 找到插入位置的前一個節點
        prev = self.dummy
        for _ in range(index):
            prev = prev.next

        # 建立新節點
        new_node = ListNode(val)
        # 先讓新節點指向右邊
        new_node.next = prev.next
        # 再讓左邊指向新節點
        prev.next = new_node
        self.size += 1

    # 找到要刪除節點前面的節點，讓它直接跳過被刪除的節點
    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        prev = self.dummy
        for _ in range(index):
            prev = prev.next
        
        prev.next = prev.next.next
        self.size -= 1       

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
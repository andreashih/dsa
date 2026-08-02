class ListNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = ListNode()  # dummy head
        self.tail = ListNode()  # dummy tail
        self.head.next = self.tail # 讓 head.next 指向 tail
        self.tail.prev = self.head # 讓 tail.prev 指向 head
        self.size = 0 # 記錄 linked list 裡目前有幾個「真正的節點」
    
    # helper function
    # 找到指定 index 的 node，並回傳那個 node，不只是值
    def _get_node(self, index: int) -> ListNode:
        # 判斷從前面還是後面找
        if index < self.size // 2:
            cur = self.head.next
            for _ in range(index):
                cur = cur.next
        else:
            cur = self.tail.prev
            for _ in range(self.size - 1 - index):
                cur = cur.prev
        return cur

    def get(self, index: int) -> int:
        # 檢查 index 是否有效
        if index < 0 or index >= self.size:
            return -1
        return self._get_node(index).val

    def addAtHead(self, val: int) -> None:
        # 加入最前面
        self.addAtIndex(0, val)        

    def addAtTail(self, val: int) -> None:
        # 加入最後面
        self.addAtIndex(self.size, val)        

    # 找到插入位置右邊的 node，然後把新 node 加到它前面
    def addAtIndex(self, index: int, val: int) -> None:
        # 這個函式不是要回傳資料，它只是修改 Linked List
        # 如果 index 不合法：直接結束函式
        if index < 0 or index > self.size:
            return
        
        if index == self.size:
            next_node = self.tail
        else:
            # 找到右邊的 node
            next_node = self._get_node(index)
        
        # 找到左邊的 node
        prev_node = next_node.prev
        # prev_node <-> new_node <-> next_node
        new_node = ListNode(val, prev_node, next_node)

        # 讓左邊指向新 node
        prev_node.next = new_node
        # 讓右邊指向新 node
        next_node.prev = new_node
        self.size += 1

    # 找到要刪除的 node，讓它左右兩邊的 node 直接連起來
    def deleteAtIndex(self, index: int) -> None:
        # 如果 index 不合法：直接結束函式
        if index < 0 or index >= self.size:
            return
        
        # 找到要刪除的 node
        node = self._get_node(index)
        # 找到左右兩邊
        prev_node = node.prev
        # 讓左右兩邊直接連接
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node
        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
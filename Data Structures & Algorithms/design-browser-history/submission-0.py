# If you visit a new page after going back, the forward history is deleted.
# You need a data structure that can efficiently:
# - move backward
# - move forward
# - erase forward history when visiting a new page

# a doubly linked list
# - each page has a pointer to the previous page
# - and a pointer to the next page

# each page in history is one node
class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val # the URL
        self.prev = prev # previous page
        self.next = next # next page

class BrowserHistory:

    def __init__(self, homepage: str):
        self.cur = ListNode(homepage) # self.cur always points to the current page        

    def visit(self, url: str) -> None:
        # current_page <-> new_page
        # if there was an old `next` page, we overwrite it
        self.cur.next = ListNode(url, self.cur) # creat a new node
        self.cur = self.cur.next # move self.cur to that new page        

    def back(self, steps: int) -> str:
        # while we still have a previous node
        # and still have steps left
        # move left
        # If you try to go back too far, you just stop at the first page
        while self.cur.prev and steps > 0:
            self.cur = self.cur.prev
            steps -= 1
        return self.cur.val        

    def forward(self, steps: int) -> str:
        while self.cur.next and steps > 0:
            self.cur = self.cur.next
            steps -= 1
        return self.cur.val

# Complexity
# - visit: O(1)
# - back: O(steps)
# - forward: O(steps)
# Space:
# - O(n) for all visited pages stored

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
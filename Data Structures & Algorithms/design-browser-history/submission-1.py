# a dynamic list + current index

class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage] # start with one page
        self.cur = 0 # pointer points at 0

    def visit(self, url: str) -> None:
        # remove all forward history
        self.history = self.history[:self.cur + 1]

        # add new page and move current pointer
        self.history.append(url)
        self.cur += 1        

    def back(self, steps: int) -> str:
        self.cur = max(0, self.cur - steps)
        return self.history[self.cur]        

    def forward(self, steps: int) -> str:
        # len(self.history) - 1: the last valide index in a python list
        self.cur = min(len(self.history) - 1, self.cur + steps)
        return self.history[self.cur]        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
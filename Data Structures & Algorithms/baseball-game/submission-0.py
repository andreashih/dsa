class Solution:
    def calPoints(self, operations: List[str]) -> int:
        myStack = []
        for op in operations:                
            if op == "+":
                myStack.append(myStack[-1] + myStack[-2])
            elif op == "D":
                myStack.append(myStack[-1] * 2)
            elif op == "C":
                myStack.pop()
            else:
                myStack.append(int(op))
        return sum(myStack)
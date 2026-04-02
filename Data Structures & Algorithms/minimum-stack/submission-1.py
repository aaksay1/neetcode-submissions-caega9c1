class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if len(self.stack) > 0:
            if(self.stack[-1] == self.min_stack[-1]):
                self.stack.pop()
                self.min_stack.pop()
            else:
                self.stack.pop()
        else:
            return "Stack is empty."

    def top(self) -> int:
        if len(self.stack) == 0:
            return "Stack is empty"
        return self.stack[-1]
        

    def getMin(self) -> int:
        if len(self.min_stack) > 0:
            return self.min_stack[-1]
        else:
            return "Stack is empty."
        
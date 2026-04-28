class MinStack:

    def __init__(self):
        self.minstack = []

    def push(self, val: int) -> None:
        self.minstack.append(val)

    def pop(self) -> None:
        self.minstack.pop()

    def top(self) -> int:
        top =  self.minstack[-1]
        return top

    def getMin(self) -> int:
        return min(self.minstack)

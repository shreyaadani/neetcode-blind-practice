class MinStack:

    def __init__(self):
        self.minstack = []
        self.mini = []

    def push(self, val: int) -> None:
        self.minstack.append(val)
        val = min(val, self.mini[-1] if self.mini else val)
        self.mini.append(val)
    def pop(self) -> None:
        self.minstack.pop()
        self.mini.pop()

    def top(self) -> int:
        top =  self.minstack[-1]
        return top

    def getMin(self) -> int:
        return self.mini[-1]

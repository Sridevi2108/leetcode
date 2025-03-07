from demo import Solution


class MyStack:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        return self.stack.pop() if self.stack else None

    def top(self) -> int:
        return self.stack[-1] if self.stack else None

    def empty(self) -> bool:
        return len(self.stack) == 0

if __name__=="__main__":
    solution=MyStack()
    print(solution.push(1))
    print(solution.push(2))
    print(solution.pop())
    print(solution.top())
    print(solution.empty())
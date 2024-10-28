class StackNode:
    def __init__(self, val: int, next_element=None):
        self.value = val
        self.next_element = next_element


class Stack:
    def __init__(self, first_element=None):
        if first_element is not None:
            self.first_element = first_element
            self.length = 1
        else:
            self.first_element = None
            self.length = 0

    def push(self, val: int) -> None:
        new_element = StackNode(val)
        new_element.next_element = self.first_element
        self.first_element = new_element
        self.length += 1

    def pop(self) -> None:
        self.first_element = self.first_element.next_element
        self.length -= 1

    def top(self) -> int:
        if self.first_element is not None:
            return self.first_element.value


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = Stack()
        j = 0
        for i in pushed:
            stack.push(i)
            while stack.length > 0 and stack.first_element.value == popped[j]:
                stack.pop()
                j += 1
        return stack.length == 0

class MyLinkedListNode:
    def __init__(self, val: int, next_element=None):
        self.value = val
        self.next_element = next_element


class MyLinkedList:
    def __init__(self, first_element=None):
        if first_element is not None:
            self.first_element = first_element
            self.length = 1
        else:
            self.first_element = None
            self.length = 0

    def getFirst(self) -> int:
        if self.first_element is not None:
            return self.first_element.value

    def addAtHead(self, val) -> None:
        new_element = MyLinkedListNode(val)
        new_element.next_element = self.first_element
        self.first_element = new_element
        self.length += 1

    def deleteFirst(self) -> None:
        self.first_element = self.first_element.next_element
        self.length -= 1


class MinStack:

    def __init__(self):
        self.main_stack = MyLinkedList()
        self.min_stack = MyLinkedList()

    def push(self, val: int) -> None:
        # add element to the start of main LL
        self.main_stack.addAtHead(val)

        # add element to the start of min LL if it is less than the current min
        if self.min_stack.length == 0 or val <= self.min_stack.getFirst():
            self.min_stack.addAtHead(val)

    def pop(self) -> None:
        # remove first element from min LL if it's value is the same as the first element of main LL
        if self.main_stack.getFirst() == self.min_stack.getFirst():
            self.min_stack.deleteFirst()

        # remove first element from main LL
        self.main_stack.deleteFirst()

    def top(self) -> int:
        # return the first element of main LL
        return self.main_stack.getFirst()

    def getMin(self) -> int:
        # return the first element of min LL
        return self.min_stack.getFirst()

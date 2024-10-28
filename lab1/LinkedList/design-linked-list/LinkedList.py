from typing import Optional


class MyLinkedListNode:
    def __init__(self, val: int, next_element: Optional["MyLinkedListNode"] = None):
        self.value = val
        self.next_element = next_element


class MyLinkedList:
    def __init__(self, first_element: Optional["MyLinkedListNode"] = None):
        if first_element is not None:
            self.first_element = first_element
            self.length = 1
        else:
            self.length = 0

    def get(self, index) -> int:
        if index >= self.length:
            return -1

        element_counter = 0
        current_element = self.first_element
        while element_counter != index:
            current_element = current_element.next_element
            element_counter += 1

        return current_element.value

    def addAtHead(self, val) -> None:
        if self.length == 0:
            self.first_element = MyLinkedListNode(val)
            self.length += 1
            return

        new_element = MyLinkedListNode(val)
        new_element.next_element = self.first_element
        self.first_element = new_element
        self.length += 1

    def addAtTail(self, val) -> None:
        new_element = MyLinkedListNode(val)

        if self.length == 0:
            self.first_element = new_element
            self.length += 1
            return

        current_element = self.first_element
        while current_element.next_element is not None:
            current_element = current_element.next_element

        current_element.next_element = new_element
        self.length += 1

    def addAtIndex(self, index, val) -> None:
        if index > self.length:
            return
        if index == self.length:
            self.addAtTail(val)
            return
        if index == 0:
            self.addAtHead(val)
            return

        element_counter = 0
        current_element = self.first_element
        while element_counter + 1 != index:
            current_element = current_element.next_element
            element_counter += 1

        new_element = MyLinkedListNode(val)
        new_element.next_element = current_element.next_element
        current_element.next_element = new_element
        self.length += 1

    def deleteAtIndex(self, index) -> None:
        if index >= self.length or index < 0:
            return

        if index == 0:
            self.first_element = self.first_element.next_element
            self.length -= 1
            return

        element_counter = 0
        current_element = self.first_element
        while element_counter + 1 != index:
            current_element = current_element.next_element
            element_counter += 1

        if current_element is not None and current_element.next_element is not None:
            current_element.next_element = current_element.next_element.next_element
            self.length -= 1

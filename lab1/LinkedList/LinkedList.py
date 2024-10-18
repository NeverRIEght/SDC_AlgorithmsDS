from typing import Optional


class LinkedListNode:
    def __init__(
            self,
            value: int,
            nextElement: Optional["LinkedListNode"] = None
    ):
        self.value = value
        self.nextElement = nextElement

    def __str__(self):
        return f"Node({self.value})"

class LinkedList:
    def __init__(
            self,
            firstElement: Optional["LinkedListNode"] = None
    ):
        if firstElement is None:
            print("Initialized new empty LinkedList")
        else:
            print("Initialized new LinkedList")
        self.firstElement = firstElement


    def fromList( # Creates a new LinkedList from a list of elements
            self,
            elements: list["LinkedListNode"] = None
    ):
        for element in elements:
            self.append(element)

        if len(elements) == 0:
            print("Initialized new empty LinkedList")
        else:
            print("Initialized new LinkedList")

    def append(self, element: LinkedListNode): # Adds an element to the end of the list
        if not isinstance(element, LinkedListNode):
            print(f"Error: wrong element type, expected: int, but was: {type(element)}")
            return None

        element = LinkedListNode(element.value)

        if self.firstElement is None:
            self.firstElement = element
            print(f"Appended: {element}")
            return

        currentElement = self.firstElement
        while currentElement.nextElement is not None:
            currentElement = currentElement.nextElement

        currentElement.nextElement = element
        print(f"Appended: {element}")

    def pop(self): # Removes and returns the last element of the list
        if self.firstElement is None:
            print("Error: can not pop from the empty LinkedList")
            return

        currentElement = self.firstElement
        previousElement = None
        while currentElement.nextElement is not None:
            previousElement = currentElement
            currentElement = currentElement.nextElement

        previousElement.nextElement = None

        print(f"Popped: {currentElement}")
        return currentElement

    def removeAllByValue(self, value: int): # Remove all elements with the specified value
        if self.firstElement is None:
            print("Error: can not remove from the empty LinkedList")
            return

        currentElement = self.firstElement
        previousElement = None
        while currentElement is not None:
            if currentElement.value == value:
                if previousElement is None:
                    self.firstElement = currentElement.nextElement
                else:
                    previousElement.nextElement = currentElement.nextElement

                print(f"Removed: {currentElement}")
                currentElement = currentElement.nextElement
                continue

            previousElement = currentElement
            currentElement = currentElement.nextElement

    def __str__(self):
        output: str = "LinkedList:\n"

        elementCounter = 0
        currentElement = self.firstElement
        while currentElement is not None:
            output += f"{elementCounter}: {currentElement}\n"

            elementCounter += 1
            currentElement = currentElement.nextElement

        return output
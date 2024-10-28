# Design a queue that supports push and pop operations in the front, middle, and back.
#
# Implement the FrontMiddleBack class:
#
#     FrontMiddleBack() Initializes the queue.
#     void pushFront(int val) Adds val to the front of the queue.
#     void pushMiddle(int val) Adds val to the middle of the queue.
#     void pushBack(int val) Adds val to the back of the queue.
#     int popFront() Removes the front element of the queue and returns it. If the queue is empty, return -1.
#     int popMiddle() Removes the middle element of the queue and returns it. If the queue is empty, return -1.
#     int popBack() Removes the back element of the queue and returns it. If the queue is empty, return -1.
#
# Notice that when there are two middle position choices, the operation is performed on the frontmost middle position choice. For example:
#
#     Pushing 6 into the middle of [1, 2, 3, 4, 5] results in [1, 2, 6, 3, 4, 5].
#     Popping the middle from [1, 2, 3, 4, 5, 6] returns 3 and results in [1, 2, 4, 5, 6].

class QueueNode:
    def __init__(self, val: int, prev_element = None, next_element = None):
        self.value = val
        self.prev_element = prev_element
        self.next_element = next_element

class FrontMiddleBackQueue:

    def __init__(self):
        self.length = 0
        self.first_element = None
        self.last_element = None

    def pushFront(self, val: int) -> None:
        if self.length == 0:
            new_element = QueueNode(val)
            self.first_element = new_element
            self.last_element = new_element
            self.length += 1
            print(f"Pushed {val} to the front")
            print(self)
            return

        new_element = QueueNode(val, next_element = self.first_element)
        self.first_element.prev_element = new_element
        self.first_element = new_element
        self.length += 1
        print(f"Pushed {val} to the front")
        print(self)

    def pushMiddle(self, val: int) -> None:
        if self.length == 0:
            new_element = QueueNode(val)
            self.first_element = new_element
            self.last_element = new_element
            self.length += 1
            print(f"Pushed {val} to the middle")
            print(self)
            return

        if self.length == 1:
            new_element = QueueNode(val, next_element=self.first_element)
            self.first_element.prev_element = new_element
            self.first_element = new_element
            self.length += 1
            print(f"Pushed {val} to the middle")
            print(self)
            return

        middle_index = self.length // 2
        element_counter = 0
        current_element = self.first_element
        while element_counter != middle_index:
            current_element = current_element.next_element
            element_counter += 1

        new_element = QueueNode(val, prev_element = current_element.prev_element, next_element = current_element)
        current_element.prev_element.next_element = new_element
        current_element.prev_element = new_element
        self.length += 1
        print(f"Pushed {val} to the middle")
        print(self)

    def pushBack(self, val: int) -> None:
        if self.length == 0:
            new_element = QueueNode(val)
            self.first_element = new_element
            self.last_element = new_element
            self.length += 1
            print(f"Pushed {val} to the back")
            print(self)
            return

        new_element = QueueNode(val, prev_element = self.last_element)
        self.last_element.next_element = new_element
        self.last_element = new_element
        self.length += 1
        print(f"Pushed {val} to the back")
        print(self)

    def popFront(self) -> int:
        if self.length == 0:
            return None
        to_return = self.first_element.value
        self.first_element = self.first_element.next_element
        self.length -= 1
        print(f"Popped {to_return} from the front")
        print(self)
        return to_return

    def popMiddle(self) -> int:
        if self.length == 0:
            print(f"Popped {None} from the middle")
            print(self)
            return None
        if self.length == 1:
            to_return = self.first_element.value
            self.first_element = None
            self.last_element = None
            self.length -= 1
            print(f"Popped {to_return} from the middle")
            print(self)
            return to_return

        middle_index = self.length // 2
        element_counter = 0
        current_element = self.first_element
        while element_counter != middle_index:
            current_element = current_element.next_element
            element_counter += 1

        to_return = current_element.value
        if current_element.prev_element is not None:
            current_element.prev_element.next_element = current_element.next_element
        if current_element.next_element is not None:
            current_element.next_element.prev_element = current_element.prev_element
        self.length -= 1
        print(f"Popped {to_return} from the middle")
        print(self)
        return to_return


    def popBack(self) -> int:
        if self.length == 0:
            print(f"Popped {None} from the back")
            print(self)
            return None
        to_return = self.last_element.value
        self.last_element.prev_element = self.last_element
        self.length -= 1
        print(f"Popped {to_return} from the back")
        print(self)
        return to_return

    def __str__(self):
        current_element = self.first_element
        result = []
        while current_element is not None:
            result.append(current_element.value)
            current_element = current_element.next_element
        return str(result)

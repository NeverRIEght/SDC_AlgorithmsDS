from LinkedList import LinkedListNode
from LinkedList import LinkedList

# First exercise: Implement the LinkedList class
# Second exercise: Implement removeAllByValue method
first = LinkedListNode(1)
second = LinkedListNode(2)
third = LinkedListNode(3)

ll = LinkedList(first)
ll.append(second)
ll.append(third)
ll.append(third)
ll.append(second)
ll.append(first)

print(ll)

ll.removeAllByValue(3)

print(ll)
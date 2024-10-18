from LinkedList import LinkedListNode
from LinkedList import LinkedList

# First exercise: Implement the LinkedList class
# Second exercise: Implement removeAllByValue method
one = LinkedListNode(1)
two = LinkedListNode(2)
three = LinkedListNode(3)
four = LinkedListNode(4)
five = LinkedListNode(5)

ll = LinkedList(one)
ll.append(two)
ll.append(three)
ll.append(four)
ll.append(five)
ll.append(two)
ll.append(four)
ll.append(five)

print(ll)

ll.removeAllByValue(1)

print(ll)

reversedLL = ll.reverse()

print(reversedLL)

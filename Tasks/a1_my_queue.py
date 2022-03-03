"""
My little Queue
"""
from typing import Any

# append()-> O(1)
# pop(-1)-> O(1)
# insert()-> O(N) кроме последнего элемента
# del -> O(N) кроме последнего элемента


class Queue:
    def __init__(self):
        self.queue = []  # начало очереди слева, конец справа

    def enqueue(self, elem: Any) -> None:
        """
        Operation that add element to the end of the queue

        :param elem: element to be added
        :return: Nothing
        """
        self.queue.append(elem)

    def dequeue(self) -> Any:
        """
        Return element from the beginning of the queue. Should return None if no elements.

        :return: dequeued element
        """
        self.queue.pop(0)

    def peek(self, ind: int = 0) -> Any:
        """
        Allow you to see at the element in the queue without dequeuing it

        :param ind: index of element (count from the beginning)
        :return: peeked element
        """
        return self.queue[ind]

    def clear(self) -> None:
        """
        Clear my queue

        :return: None
        """
        self.queue.clear
    def __str__(self):
        return str(self.queue)

a = Queue()
a.enqueue(3)
a.enqueue(4)
a.enqueue(5)
a.enqueue(6)
print(a)
a.dequeue()
print(a)
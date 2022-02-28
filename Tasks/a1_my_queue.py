"""
My little Queue
"""
from typing import Any


class Queue:
    def __init__(self):
        self.queue = []  # todo для очереди можно использовать python list

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
        if not self.queue:
            return None
        return self.queue.pop()

    def peek(self, ind: int = 0) -> Any:
        """
        Allow you to see at the element in the queue without dequeuing it

        :param ind: index of element (count from the beginning)
        :return: peeked element
        """
        reversed_index = -ind - 1
        if not self.queue:
            return None
        if ind > len(self.queue) - 1:
            return None
        return self.queue[int]



    def clear(self) -> None:
        """
        Clear my queue

        :return: None
        """
        self.queue.clear()

    def __str__(self):
        return(str(self.queue))

a = Queue()
for i in range(10):
    a.enqueue(i)
print(a)
"""
Priority Queue

Queue priorities are from 0 to 10
"""
from typing import Any


class PriorityQueue:
    def __init__(self):
        self.priorityqueue = []  # todo для очереди можно использовать python dict

    def enqueue(self, elem: Any, priority: int = 0) -> None:
        """
        Operation that add element to the end of the queue

        :param elem: element to be added
        :return: Nothing
        """
        item = {
            "elem": elem,
            "priority": priority
        }
        if not self.priorityqueue:
            self.priorityqueue.append(item)

        for index, current_item in enumerate(self.priorityqueue):
            if item["priority"] >= current_item["priority"]:
                self.priorityqueue.insert(index, item)
                break
        else:
            self.priorityqueue.append(item)





    def dequeue(self) -> Any:
        """
        Return element from the beginning of the queue. Should return None if not elements.

        :return: dequeued element
        """
        if not self.priorityqueue:
            return None
        return self.priorityqueue.pop()['elem']

    def peek(self, ind: int = 0, priority: int = 0) -> Any:
        """
        Allow you to see at the element in the queue without dequeuing it

        :param ind: index of element (count from the beginning)
        :return: peeked element
        """
        return None

    def clear(self) -> None:
        """
        Clear my queue

        :return: None
        """
        self.priorityqueue.clear()

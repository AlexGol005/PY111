"""
My little Stack
"""
from typing import Any


class Stack:
    def __init__(self):
        self.stack = []  # todo для стека можно использовать python list

    def push(self, elem: Any) -> None:
        """
        Operation that add element to stack

        :param elem: element to be pushed
        :return: None
        """
        self.stack.append(elem)


    def pop(self) -> Any:
        """
        Pop element from the top of the stack. If not elements - should return None.

        :return: popped element
        """
        if not self.stack:
            return None
        return self.stack.pop()

    def peek(self, ind: int = 0) -> Any:
        """
        Allow you to see at the element in the stack without popping it.

        :param ind: index of element (count from the top, 0 - top, 1 - first from top, etc.)
        :return: peeked element or None if no element in this place
        """
        #reversed_stack = reversed(self.stack)
        reversed_index = -ind - 1
        if len(self.stack) == 0:
            return None
        if ind == 0:
            reversed_index = len(self.stack) - 1
        if ind > len(self.stack) - 1:
            raise ValueError
        return self.stack[reversed_index]



    def clear(self) -> None:
        """
        Clear my stack

        :return: None
        """
        self.stack.clear()

from Tasks.a0_my_stack import Stack

def check_brackets(brackets_row: str) -> bool:
    """
    Check whether input string is a valid bracket sequence
    Valid examples: "", "()", "()()(()())", invalid: "(", ")", ")("
    :param brackets_row: input string to be checked
    :return: True if valid, False otherwise
    """
    store = Stack()
    for i in brackets_row:
        if i == '(':
            store.push(i)
        if i == ')':
            if not store.stack:
                return False
            store.pop()
    if not store.stack:
        return True
    return False

print(check_brackets('(()))'))





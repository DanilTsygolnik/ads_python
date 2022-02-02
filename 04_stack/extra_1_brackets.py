from stack import Stack

def check_balance(str_with_brackets: str) -> str:
    open_brackets = Stack()
    close_brackets = Stack()
    for i in str_with_brackets:
        if i == "(":
            open_brackets.push(i)
        if i == ")":
            close_brackets.push(i)
    if open_brackets.size() == close_brackets.size():
        return "String is balanced"
    return "String is not balanced"

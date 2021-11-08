from deque import Deque

def palindrome(test_str: str) -> bool:
    if test_str == "":
        raise ValueError('String is empty')
    dq = Deque()
    for i in test_str:
        dq.addTail(i)
    cnt = dq.size() % 2
    while dq.size() > cnt:
        head = dq.removeFront()
        tail = dq.removeTail()
        if head != tail:
            return False
    return True
